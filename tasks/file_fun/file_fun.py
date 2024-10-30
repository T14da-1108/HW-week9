from typing import List


def first_n_lines(filename: str, n: int) -> List[str]:
    """
    Function that returns first n lines (including \\n delimiter).
    Checks whether file is a file and readable, and also that
    n is non-negative, throws error if it is not true.

    :param filename: The path to the file.
    :param n: The number of lines.
    :return: A list containing first n lines in
             the file (including \\n delimiter).
    """
    pass


def last_n_lines(filename: str, n: int) -> List[str]:
    """
    Returns the last n lines of the specified file.
    Checks whether file is a file and readable, and also that
    n is non-negative, throws error if it is not true.

    :param filename: The path to the file.
    :param n: The number of lines.
    :return: A list of the last n lines in the file
             (including \\n delimiter).
    """
    pass


def append_text(filename: str, text: str) -> None:
    """
    Appends the specified text to the end of the file.
    Checks whether file is a file and writeable,
    throws error if it is not true.

    :param filename: The path to the file.
    :param text: The text to append to the file.
    """
    pass
