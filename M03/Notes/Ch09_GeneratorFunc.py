Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def my_range(first=0, last=10, step=1):
...     number = first
...     while number < last:
...         yield number
...         number += step
... 
...         
>>> my_range
<function my_range at 0x0000018D850B58A0>
>>> ranger = my_range(1,5)
>>> ranger
<generator object my_range at 0x0000018D85075970>
>>> for x in ranger:
...     print(x)
... 
...     
1
2
3
4
>>> for try_again in ranger:
...     print(try_again)
... 
...     
