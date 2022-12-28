import os
import json
import shutil

from typing import List, Dict, Any


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

    for item in json_content:
        full_path = path + "/" + f"sales_{data}_{index}.json"
        with open(full_path, 'w') as fp:
            json.dump(item, fp)
        index += 1
