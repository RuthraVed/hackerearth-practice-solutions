import json
from pathlib import Path

import requests

SAVE_DIR = Path.cwd() / Path("saved_files")
SAVE_DIR.mkdir(parents=True, exist_ok=True)


def read_json(json_path):
    json_text = ""
    # if a URL is given as json_path
    if "http" in json_path and ".com" in json_path:
        json_text = requests.get(json_path).text
    else:
        json_path = Path(json_path)
        if json_path.is_file():
            with open(json_path, "r") as f:
                json_text = f.read()
    return json_text


def prettify_json(json_text, indent=4):
    # Convert JSON text to Python Types and Pretty print JSON data
    """
    Note:
    i)  json.loads() used to parse a json string/text
    ii) json.load() used to parse a json file object
    """
    obj = json.loads(json_text)
    pretty_json = json.dumps(obj, indent=indent)
    return pretty_json


def save_json_file(json_path, save_name="raw_data_list", save_dir=SAVE_DIR):
    pretty_json = []

    # Loading json from source URL/path
    json_text = read_json(json_path)

    # Prettify JSON data
    pretty_json = prettify_json(json_text)

    # Save to a file
    with open(Path(save_dir) / Path(save_name + ".json"), mode="w", encoding="utf-8") as f:
        f.write(pretty_json)


def extract_station_details(json_text, save_as_json=False, save_name="station_details", save_dir=SAVE_DIR):
    details_dict = json.loads(json_text)["Data"]

    station_dict = {}
    for i, station in enumerate(details_dict):
        station_seq = f"Station {i+1:02}"

        sub_station_list = []
        temp_dict = {}
        for j, sub_station in enumerate(station["Locations"]):
            sub_station_list.append(sub_station["Name"])

        temp_dict[station["Name"]] = sub_station_list
        station_dict[station_seq] = temp_dict

    if save_as_json:
        # Prettify JSON data
        pretty_json = json.dumps(station_dict, indent=4)

        # Save to a file
        with open(Path(save_dir) / Path(save_name + ".json"), mode="w", encoding="utf-8") as f:
            f.write(pretty_json)

    return station_dict


if __name__ == "__main__":

    JSON_SOURCE = "http://fgregxapp2.jdnet.deere.com/GXPRFS/Line/MRN159569/Station/"

    save_json_file(json_path=JSON_SOURCE)

    json_text = read_json(json_path=JSON_SOURCE)
    results_list = extract_station_details(json_text, save_as_json=True)
    print(results_list)
