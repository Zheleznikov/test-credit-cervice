import json


def parse_json(path):
    with open(path) as md:
        return json.load(md)


def get_couple_source_res(cell):
    return [
        tuple(i.values())
        for i in list(cell.values())
    ]


def get_only_source(key, cell):
    return [i[key] for i in list(cell.values())]


def get_one_value(cell):
    return [i for i in list(cell.values())]