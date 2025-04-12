Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def knights2(saying):
...     def inner2():
...         return "We are the knights who say: '%s'" % saying
...     return inner2
... 
>>> a = knights2('Duck')
>>> b = knights2('Hasenpfeffer')
>>> type(a)
<class 'function'>
>>> type(b)
<class 'function'>
>>> a
<function knights2.<locals>.inner2 at 0x105560d60>
>>> b
<function knights2.<locals>.inner2 at 0x105560ea0>
>>> a()
"We are the knights who say: 'Duck'"
>>> b()
"We are the knights who say: 'Hasenpfeffer'"
>>> def edit_story(words, funct):
...     for word in words:
...         print(func(word))
... 
...         
>>> stairs = ['thud', 'meow', 'thud', 'hiss']
>>> 
>>> def enliven(word): # give that prose more punch
