Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def answer():
    print(42)

    
answer()
42
def run_something(func):
    func()

    
run_something(answer)
42
type(run_something)
<class 'function'>
def add_args(arg1, arg2):
    print(arg1 + arg2)

    
type(add_args)
<class 'function'>
def lets_run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

    
>>> run_somthing_with_args(add_args, 5,9)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    run_somthing_with_args(add_args, 5,9)
NameError: name 'run_somthing_with_args' is not defined. Did you mean: 'lets_run_something_with_args'?
>>> lets_run_something_with_args(add_args, 5,9)
14
>>> def sum_args(*args):
...     return sum(args)
... 
>>> def run_with_positional_args(func, *args):
...     return func(*args)
... run_with_positional_args(sum_args, 1,2,3,4)
SyntaxError: invalid syntax
>>> run_with_positional_args(sum_args,1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    run_with_positional_args(sum_args,1,2,3,4)
NameError: name 'run_with_positional_args' is not defined
>>> def run_with_positional_args(func,*args):
...     return func(*args)
... 
>>> run_with_positional_args(sum_args,1,2,3,4)
10
>>> def outer(a,b):
...     def inner(c,d):
...         return c+d
...     return inner(a,b)
... 
>>> outer(4,7)
11
>>> def knights(saying):
...     def inner(quote):
...         return "We are the knights who say: '%s'" % quote
...     return inner(saying)
... 
>>> knights('Ni!')
"We are the knights who say: 'Ni!'"
