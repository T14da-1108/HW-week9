import json
import csv


def json_to_csv(json_filename: str, csv_filename: str) -> None:
    """
    Converts a JSON file containing a list of records with
    the same set of keys to a corresponding CSV file.

    Example:

    `[{"name": "Denis", "age": 21}, {"name": "Rodion", "age": 20}]`

    transforms to

    name,age
    Denis,21
    Rodion,20

    :param json_filename: The name of JSON file to convert.
    :param csv_filename: The name of CSV file to write converted JSON to.
    """

    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)  # JSONデータをPythonリストに変換

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for record in data:
            writer.writerow(record)
