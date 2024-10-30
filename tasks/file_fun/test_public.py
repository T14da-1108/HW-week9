from pathlib import Path
from typing import Callable

import pytest

from .file_fun import first_n_lines, last_n_lines, append_text


@pytest.fixture
def create_temp_file(tmp_path: Path) -> Callable[[str], Path]:
    def _create_temp_file(content: str) -> Path:
        file = tmp_path / "test.txt"
        file.write_text(content)
        return file

    return _create_temp_file


@pytest.mark.parametrize("content, n, expected", [
    ("first line\nsecond line\nthird line\n", 2, ["first line\n", "second line\n"]),
    ("line1\nline2\nline3\nline4\n", 3, ["line1\n", "line2\n", "line3\n"]),
    ("a\nb\nc\n", 1, ["a\n"])
])
def test_first_n_lines(create_temp_file: Callable[[str], Path], content: str, n: int, expected: str) -> None:
    temp_file = create_temp_file(content)
    assert first_n_lines(str(temp_file), n) == expected


@pytest.mark.parametrize("content, n, expected", [
    ("first line\nsecond line\nthird line\n", 2, ["second line\n", "third line\n"]),
    ("line1\nline2\nline3\nline4\n", 3, ["line2\n", "line3\n", "line4\n"]),
    ("a\nb\nc\n", 1, ["c\n"])
])
def test_last_n_lines(create_temp_file: Callable[[str], Path], content: str, n: int, expected: str) -> None:
    temp_file = create_temp_file(content)
    assert last_n_lines(str(temp_file), n) == expected


@pytest.mark.parametrize("initial_content, text_to_append, expected_final_content", [
    ("line1\nline2\n", "new line\n", ["line1\n", "line2\n", "new line\n"]),
    ("a\nb\n", "c\n", ["a\n", "b\n", "c\n"]),
    ("", "first line\n", ["first line\n"])
])
def test_append_text(
    create_temp_file: Callable[[str], Path],
    initial_content: str,
    text_to_append: str,
    expected_final_content: str
) -> None:
    temp_file = create_temp_file(initial_content)
    append_text(str(temp_file), text_to_append)

    with open(temp_file, "r") as f:
        final_content = f.readlines()
    assert final_content == expected_final_content

