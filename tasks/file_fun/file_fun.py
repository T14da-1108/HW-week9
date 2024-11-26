from typing import List


def first_n_lines(filename: str, n: int) -> List[str]:
    if n < 0:
        raise ValueError("Number of lines to read must be non-negative.")

    try:
        with open(filename, "r") as file:
            lines = [next(file) for _ in range(n)]
            return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    except IOError:
        raise IOError(f"The file '{filename}' could not be read.")
    except StopIteration:
        return lines

def last_n_lines(filename: str, n: int) -> List[str]:
    if n < 0:
        raise ValueError("Number of lines to read must be non-negative.")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            return lines[-n:] if n <= len(lines) else lines
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    except IOError:
        raise IOError(f"The file '{filename}' could not be read.")

def append_text(filename: str, text: str) -> None:
    try:
        with open(filename, "a") as file:
            file.write(text)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    except IOError:
        raise IOError(f"The file '{filename}' could not be written to.")
