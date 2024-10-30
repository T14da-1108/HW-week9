## INPUT_ (2 POINTS)

`io` `stdin` `stdout` `readline` `raise`

### Task

Write your own version of built-in `input()` function  
with a twist. Unlike Python's `input()`, your implementation
should support arbitrary IO streams. Thus, your function
should print input prompt `prompt` to the `out` stream, read
a line from the `inp` stream and return it. See the details
in the docstring.

### Example

```python
>>> input_('login: ')
login: guido
'guido'
>>> input_('password: ', inp=io.StringIO('ilovepython'))
password: 'ilovepython'
>>> input_('password: ', inp=io.StringIO()) is None
password: True
```

### Notes

* Obviously, built-in `input()` cannot be used — we check for 
this.
* If [`Ctrl+D`](https://en.wikipedia.org/wiki/End-of-Transmission_character) was pressed, 
the function should return `None`. To determine whether
`Ctrl+D` has been pressed, carefully look at what the 
`readline` stream method will return in this case.
* Considering the weird task name -- to avoid collision with
keywords and built-in functions, sometimes the name of a 
variable/function/class ends with an underscore.
You might come across names like `type_`, `class_` 
when reading other's code.
* Don't change `import sys` to `from sys import stdin`,
otherwise monkeypatch in the tests will fail.
