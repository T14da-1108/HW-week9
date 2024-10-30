## COUNT UTIL (3 POINTS)

`argparse` `split` `interview`

### Task

Implement UNIX console application __wc__ in the form of `count_util` function which accepts
text input and following flags as strings:
* `-m` - number of characters;
* `-l` - number of lines;
* `-L` - the length of the longest line;
* `-w` - number of words.

If no flags were supplied, we assume that each one of 
them is activated: `-m -l -L -w`.

Keep in mind that flags could be joined together in
any order: `-lmL` is a correct flags string.

The input text can contain from 0 to 100 lines.

Your implementation returns a dictionary:
* `chars` - number of characters;
* `lines` - number of lines;
* `longest_line` - the length of the longest line;
* `words` - number of words.

Of course, using the console utility __wc__ in this task is forbidden (and it won't be much easier).

NB: According to the __wc__ documentation: _A line is defined as a string of characters delimited by a <newline>
character. A word is defined as a string of characters delimited by white space characters_.
I.e., **it is necessary to take the last line break into account**.


### Example
```python
>>> text = '''\
there is one
    more
example for
 problem
'''
>>> count_utils(text, flags=None)
{'lines': 4, 'words': 7, 'chars': 43, 'longest_line': 12}
```

### Additional Comments
This task is an exercise on strings and parsing command line arguments. You might as well get something like this on a job interview.

The most 'classic' library for creating CLI (command-line interface) is
built-in [argparse](https://docs.python.org/3/library/argparse.html) library.  
But it is definitely not the most convenient. Consider  [click](https://click.palletsprojects.com/en/latest/) library, which allows you to create CLI much faster and more conveniently.

You need to figure this out on your own.

