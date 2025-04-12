Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = 7
x == 5
False
x == 7
True
5 < x
True
x < 10
True
5 < x and x < 10
True
x < 10 and x < 5
False
5 < x or x < 10
True
>>> x < 10 and 5 < x
True
>>> 5 < x and x > 10
False
>>> 5 < x and not x > 10
True
>>> 5 < x < 10
True
>>> boolean
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    boolean
NameError: name 'boolean' is not defined
>>> false
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> False
False
>>> None
>>> some_list = []
>>> if some_list:
...     print("There's something in here")
... else:
...     print("Hey, it's empty!")
... 
...     
Hey, it's empty!
>>> letter = 'o'
>>> if letter == 'a' or letter == 'e' or letter == 'i'\
...    or letter == 'o' or letter == 'u':
...     print(letter, 'is a vowel')
... else:
...     print(letter, 'is not a vowel')
... 
...     
o is a vowel
