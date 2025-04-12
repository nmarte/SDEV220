Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def edit_story(words, func):
    for word in words:
        print(func(word))

        
stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word): # give that prose more punch
    return word.capitalize() + '!'

edit_story(stairs, enliven)
Thud!
Meow!
Thud!
Hiss!
edit_story(stairs, lambda word: word.capitalize() + '!')
Thud!
Meow!
Thud!
Hiss!
def document_it(func):
    def new_function(*args, **kwargs):
...         print('Running cuntion:', func.__name__)
...         print('Positional arguments:', args)
...         print('Keyword arguments:', kwargs)
...         result = funct(*args, **kwargs)
...         print('Result:', result)
...         return result
...     return new_function
... 
>>> def add_ints(a,b):
...     return a + b
... 
>>> add_ints(3,5)
8
>>> cooler_add_ints = document_it(add_ints) # manual decorator assignment
>>> cooler_add_ints(3,5)
Running cuntion: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    cooler_add_ints(3,5)
  File "<pyshell#20>", line 6, in new_function
    result = funct(*args, **kwargs)
NameError: name 'funct' is not defined
>>> @document_it
... def add_ints(a,b):
...     return a + b
... 
>>> add_ints(3,5)
Running cuntion: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    add_ints(3,5)
  File "<pyshell#20>", line 6, in new_function
    result = funct(*args, **kwargs)
NameError: name 'funct' is not defined
