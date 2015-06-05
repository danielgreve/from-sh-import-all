# Use Python As A Pseudo-Shell With `sh`

## How To Run

First confirm the `sh` module is installed, or install with `pip`.

```python
python -i from-sh-import-all.py

# Alternatively, for filename tab completion
ipython -i from-sh-import-all.py
```

## Examples

```python
>>> ls()
LICENCE.md              README.md               from-sh-import-all.py

>>> git.init("README.md")

>>> echo("Hello")
Hello

>>> 
```

## Why Would You Want To Do This?

Honestly, you likely would not. Python syntax is terse, but not terse enough for a great shell experience. Plus, `sh` does not implement interactive applications [yet](https://github.com/amoffat/sh/issues/92), so vim and the like would not be available unless you defined functions for them like so:

```
def vim(filename)
    os.system("vim {}".format(filename))

```

Altogether, IPython provides a better interactive experience for system shell usage along with Python. However, `sh` is a godsend for scripting with shell commands.

## Further Reading

* `sh` [documentation](https://amoffat.github.io/sh/)
* [IPython as a system shell](http://ipython.org/ipython-doc/stable/interactive/shell.html)
