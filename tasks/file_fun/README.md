## FILE FUN (2 POINTS)

`file handling` `read` `write`

### Task

Implement the following functions related to file manipulation.
Assert that files always have correct number of lines, not less
than our tests ask you to extract.

test.txt:
```plaintext
first line
second line
third line
fourth line
fifth line
```

**1. `first_n_lines`**:  
Write a function that accepts a filename and returns the first n lines of the file.

```python
>>> first_n_lines('test.txt', 3)
['first line\n', 'second line\n', 'third line\n']
```

**2. `last_n_lines`**:  
Create a function that accepts a filename and returns the last n lines of the file.

```python
>>> last_n_lines('test.txt', 3)
['third line\n', 'fourth line\n', 'fifth line\n']
```

**3. `append_text`**:  
Implement a function that accepts a filename and appends text to the file.

```python
>>> append_text('test.txt', 'sixth line\n')
```

test.txt:
```plaintext
first line
...
sixth line
```
`...` represents the lines that were not shown.

### About the Task

These tasks are a good introduction to file handling in Python, and they cover basic operations such as reading from and writing to a file. These are fundamental skills for any Python developer and used by me at somewhat daily basis.
