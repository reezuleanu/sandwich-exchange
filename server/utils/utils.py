import json
from bson import BSON, json_util


def bson2dict(bson: BSON) -> dict:
    """Function that converts bson to json

    Args:
        bson (BSON): bson data to be converted

    Returns:
        dict: converted data
    """

    return json.loads(json_util.dumps(bson))
