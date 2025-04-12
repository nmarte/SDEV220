Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def echo(anything):
...     'echo returns its input argument'
...     return anything
... 
>>> def print_if_true(thing, check):
...     '''
...     Prints the first argument if a second argument is true.
...     the operation is:
...         1. Check whether the *second* argument is true.
...         2. If it is, print the *first* argument.
...     '''
...     if check:
...         print(thing)
... 
...         
>>> help(echo)
Help on function echo in module __main__:

echo(anything)
    echo returns its input argument

>>> print(echo.__doc__)
echo returns its input argument
