import ast
import inspect
import io
import pathlib
import sys

import pytest

from .input_ import input_


def test_structural() -> None:
    source = inspect.getsource(input_)
    tree = ast.parse(source)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue

        if isinstance(node.func, ast.Name):
            assert node.func.id != "input", "Your implementation contains built-in input function"


@pytest.mark.parametrize('prompt,user_input', [
    ('> ', '1+1'),
    ('>> ', 'The quick brown fox jumps over the lazy dog.'),
    ('>>> ', 'Dear John'),
    ('', "    'whitespace'  "),
])
def test_basic(prompt: str, user_input: str) -> None:
    inp = io.StringIO(user_input + '\n')
    out = io.StringIO()
    assert input_(prompt, inp, out) == user_input
    assert out.getvalue() == (prompt or '')


def test_eof() -> None:
    inp = io.StringIO()
    out = io.StringIO()
    assert input_(None, inp, out) is None
    assert out.getvalue() == ''


def test_eof_with_prompt() -> None:
    inp = io.StringIO()
    out = io.StringIO()
    assert input_('$ ', inp, out) is None
    assert out.getvalue() == '$ '


def test_stdin_stdout(capsys, monkeypatch):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO('guido\n'))
    assert input_('login: ') == 'guido'
    captured = capsys.readouterr()
    assert captured.out == 'login: '
    assert captured.err == ''


def test_prompt_flushed(tmp_path: pathlib.Path) -> None:
    inp_path = tmp_path / 'inp'
    inp_path.write_text('something')
    out_path = tmp_path / 'out'

    with inp_path.open('r') as inp:
        with out_path.open('w') as out:
            prompt = '(the prompt)> '
            input_(prompt, inp, out)
            assert out_path.read_text() == prompt
