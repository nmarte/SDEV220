Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def do_nothing():
...     pass
... do_nothing()
SyntaxError: invalid syntax
>>> do_nothing()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    do_nothing()
NameError: name 'do_nothing' is not defined
>>> do_nothing()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    do_nothing()
NameError: name 'do_nothing' is not defined
>>> def make_a_sound():
...     print('quack')
... 
...     
>>> make_a_sound
<function make_a_sound at 0x1012c5120>
>>> make_a_sound()
quack
