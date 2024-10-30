from pathlib import Path
from typing import Callable, Tuple, Any

import pytest
import os

from .json_to_csv import json_to_csv


@pytest.fixture
def create_io_files(tmp_path: Path) -> Callable[[str], Tuple[Path, Path, Path]]:
    def _create_io_files(testname: str) -> Tuple[Path, Path, Path]:
        test_data = Path(__file__).resolve().parent / "test_data"

        json_file = tmp_path / "test.json"
        print(os.getcwd())
        with open(test_data / (testname + ".json"), "r") as fin:
            json_file.write_text(fin.read())

        csv_file_answer = tmp_path / "test.csv"

        csv_file_gold = tmp_path / "test.csv.gold"
        with open(test_data / (testname + ".csv"), "r") as fin:
            csv_file_gold.write_text(fin.read())

        return json_file, csv_file_answer, csv_file_gold

    return _create_io_files


@pytest.mark.parametrize("testname", [
    "simple",
    "single_value",
    "values_with_commas"
])
def test_simple(
    create_io_files: Callable[[str], Tuple[Path, Path, Path]],
    testname: str
) -> None:
    json_file, csv_file_answer, csv_file_gold = create_io_files(testname)
    json_to_csv(str(json_file), str(csv_file_answer))

    assert csv_file_answer.exists(), "Your implementation doesn't create a new file"

    with open(csv_file_answer, "r") as expected:
        with open(csv_file_gold, "r") as actual:
            assert expected.read().strip() == actual.read().strip()
