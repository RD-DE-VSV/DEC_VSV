import os
import json
import shutil

from fastavro import writer, parse_schema

from typing import List, Dict, Any


def open_from_disk(path: str) -> List[Dict[str, Any]]:
    """
    Read data at specific path

    :param path: path to source dir
    """

    result = []
    should_fetch_next_file = True
    data = os.path.basename(os.path.normpath(path))
    index = 1

    while should_fetch_next_file:
        full_path = path + "/" + f"sales_{data}_{index}.json"
        if os.path.exists(full_path):
            with open(full_path, 'r') as fp:
                result.append(json.load(fp))
            index += 1
        else:
            should_fetch_next_file = False

    return result


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    """
    Save data at specific path

    :param json_content: list of records
    :param path: path to target dir
    """

    if os.path.isdir(path):
        shutil.rmtree(path)

    os.mkdir(path)

    data = os.path.basename(os.path.normpath(path))
    index = 1

    schema = {
        'name': 'Sales',
        'type': 'record',
        'fields': [
            {'name': 'client', 'type': 'string'},
            {'name': 'purchase_date', 'type': 'string'},
            {'name': 'product', 'type': 'string'},
            {'name': 'price', 'type': 'int'},
        ],
    }
    parsed_schema = parse_schema(schema)

    for item in json_content:
        full_path = path + "/" + f"sales_{data}_{index}.avro"
        with open(full_path, 'wb') as fp:
            writer(fp, parsed_schema, item)
        index += 1
