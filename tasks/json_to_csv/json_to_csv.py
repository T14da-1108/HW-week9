def json_to_csv(json_filename: str, csv_filename: str) -> None:
    """
    Converts a JSON file containing a list of records with
    the same set of keys to a corresponding CSV file.

    Example:

    `[{"name": "Denis", age: 21}, {"name": "Rodion", age: 20}]`

    transforms to

    name,age\n
    Denis,21\n
    Rodion,20

    :param json_filename: The name of JSON file to convert.
    :param csv_filename: The name of CSV file to write converted JSON to.
    """
