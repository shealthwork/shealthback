import json
from collections import OrderedDict


def parse_json_data(data_str):
    """
    Converts any stringfied data into json data using json library

    Input
    -----
    data_str   - Data in json string format

    Output
    ------
    status_obj  - Status obj
    json_data   - Python dictionary format of the given json data
    """

    # Convert this file data into json data
    try:
        json_data = json.loads(data_str, object_pairs_hook=OrderedDict)

    except ValueError as json_err_msg:

        print("Error in input json format %s\n" % data_str)
        print("Json parsing error %s\n" % json_err_msg)

        return ""

    return json_data