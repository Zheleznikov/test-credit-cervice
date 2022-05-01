import pytest

from consts.hosts import local_host, heroku_host


def pytest_addoption(parser):
    parser.addoption("--bench", action="store", default="heroku")


@pytest.fixture(scope="function")
def bench(request):
    if request.config.getoption("bench") == "local":
        return local_host
    elif request.config.getoption("bench") == "heroku":
        return heroku_host
