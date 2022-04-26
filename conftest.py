import pytest

from consts.hosts import local_host


def pytest_addoption(parser):
    parser.addoption("--bench", action="store", default="local")


@pytest.fixture(scope="function")
def bench(request):
    if request.config.getoption("bench") == "local":
        return local_host
