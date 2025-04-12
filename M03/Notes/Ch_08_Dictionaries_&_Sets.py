Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
empty_dict = {}
empty_dict
{}
bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive":"Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
    }
bierce
{'day': 'A period of twenty-four hours, mostly misspent', 'positive': "Mistaken at the top of one's voice", 'misfortune': 'The kind of fortune that never misses'}
acme_customer = {'first':'Wile', 'middle':'E', 'last':'Cayote'}
acme_customer
{'first': 'Wile', 'middle': 'E', 'last': 'Cayote'}
acme_cusotmer = dict(first = "Wile", middle = "E", last = 'Cayote')
acme_customer
{'first': 'Wile', 'middle': 'E', 'last': 'Cayote'}
lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f']]
dict(lol)
{'a': 'b', 'c': 'd', 'e': 'f'}
los = ['ab', 'cd', 'ef']
dict(los)
{'a': 'b', 'c': 'd', 'e': 'f'}
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}
pythons['Gilliam'] = 'Gerry'
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Gerry'}
pythons['Gilliam']='Terry'
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry'}
some_pythons['John']
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    some_pythons['John']
NameError: name 'some_pythons' is not defined
some_pythons = {
    'Graha': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
    }
some_pythons
{'Graha': 'Chapman', 'John': 'Cleese', 'Eric': 'Idle', 'Terry': 'Jones', 'Michael': 'Palin'}
some_pythons['John']
'Cleese'
'Groucho' in some_pythons
False
some_pythons.get('John')
'Cleese'
some_pythons.get('Groucho', 'Not a Python')
'Not a Python'
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
signals.keys()
dict_keys(['green', 'yellow', 'red'])
list(signals.values())
['go', 'go faster', 'smile for the camera']
list(signals.items())
[('green', 'go'), ('yellow', 'go faster'), ('red', 'smile for the camera')]
len(signals)
3
first = {'a', 'agony': 'b':'bliss'}
SyntaxError: invalid syntax
first
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    first
NameError: name 'first' is not defined. Did you mean: 'list'?
first = {'a':'agony', 'b':'bliss'}
second = {'b':'bagels', 'c':'candy'}
{**first, **second}
{'a': 'agony', 'b': 'bagels', 'c': 'candy'}
third = {'d':'donuts'}
{**first, **third, **second}
{'a': 'agony', 'b': 'bagels', 'd': 'donuts', 'c': 'candy'}
pythons = "
SyntaxError: unterminated string literal (detected at line 1)
pythons = {
    'Chapman':'Graham',
    'Cleese':'John',
    'Gilliam':'Terry',
    'Idle':'Eric',
    'Jones':'Terry',
    'Palin':'Michael',
    }
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}
others = {'Marx':'Groucho', 'Howard':'Moe'}
pythons.update(others)
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Marx': 'Groucho', 'Howard': 'Moe'}
del pythons['Marx']
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Howard': 'Moe'}
del pythons['Howard']
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}
len(pythons)
6
pythons.pop('Palin')
'Michael'
len(pythns)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    len(pythns)
NameError: name 'pythns' is not defined. Did you mean: 'pythons'?
len(pythons)
5
pythons.pop('Palin')
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    pythons.pop('Palin')
KeyError: 'Palin'
pythons.pop('First', 'Hugo')
'Hugo'
len(pythons)
5
pythons.clear()
pythons
{}
pythons = {}
pythons
{}
pythons = {'Chapman':'Graham', 'Cleese':'John', 'Jones':'Terry', 'Palin':'Michael', 'Idle':'Eric'}
'Chapman' in pythons
True
'Palin' in pythons
True
'Gilliam' in pythons
False
signals
{'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
save_signals
{'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera', 'blue': 'confuse everyone'}
signals = {'green':'go', 'yellow':'go faster', 'red':'smile for the camera'}
original_signals = signals.copy()
signals['blue']='confuse everyone'
signals
{'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera', 'blue': 'confuse everyone'}
original_signals
{'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
signals = {'green':'go',
           'yellow':'go faster',
           'red':['stop', 'smile']}
signals_copy = signals.copy()
signals
{'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
signals_copy
{'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
signals['red'][1] = 'sweat'
signals
{'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'sweat']}
signals_copy
{'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'sweat']}
import copy
signals = {'green':'go',
           'yellow':'go faster',
           'red':['stop','smile']}
signals_copy = copy.deepcopy(signals)
signals
{'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
signals_copy
{'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
signals['red'][1]=
SyntaxError: invalid syntax
signals['red'][1]='sweat
SyntaxError: unterminated string literal (detected at line 1)
signals['red'][1] = 'sweat'
signals
{'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'sweat']}
signals_copy
{'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
a == b
True
a <= b
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    a <= b
TypeError: '<=' not supported between instances of 'dict' and 'dict'
a = {1:[1,2], 2:[1], 3:[1]}
b = {1:[1,1], 2:[1], 3:[1]}
a == b
False
accusation = {'room':'ballroom', 'weapon':'lead pipe',
              'person':'Col. Mustard'}
for card in accusation: # or, for card in accusation.keys():
    print(card)

    
room
weapon
person
for value in accusation.values():
    print(value)

    
ballroom
lead pipe
Col. Mustard
for item in acussation.items():
    print(item)

    
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    for item in acussation.items():
NameError: name 'acussation' is not defined. Did you mean: 'accusation'?
for item in accusation.items():
    print(item)

    
('room', 'ballroom')
('weapon', 'lead pipe')
('person', 'Col. Mustard')
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

    
Card room has the contents ballroom
Card weapon has the contents lead pipe
Card person has the contents Col. Mustard
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts
{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}
letter_counts = {letter: word.count(letter) for letter in set(word)}
letter_counts
{'l': 1, 's': 1, 'r': 1, 'e': 2, 't': 2}
vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter:word.count(letter) for letter in set(word)}
vowel_counts = {letter:word.count(letter) for letter in set(word)
                if letter in vowels}
vowel_counts
{'a': 2, 'i': 1, 'o': 4, 'e': 1}
empty_set = set()
empty_set
set()
even_numbers = {0, 2, 4, 6, 8}
even_nubers
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    even_nubers
NameError: name 'even_nubers' is not defined. Did you mean: 'even_numbers'?
even_numbers
{0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers
{1, 3, 5, 7, 9}
set('letters')
{'l', 's', 'r', 'e', 't'}
set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
{'Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'}
set(('Ummagumma', 'Echoes', 'Atom Heart Mother'))
{'Atom Heart Mother', 'Ummagumma', 'Echoes'}
set({'apple':'red', 'orange':'orange', 'cherry':'red'})
{'apple', 'orange', 'cherry'}
reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
len(reindeer)
4
s = set((1,2,3))
s
{1, 2, 3}
s.add(4)
s
{1, 2, 3, 4}
s.remove(3)
s
{1, 2, 4}
furniture = set(('sofa', 'ottoman', 'table'))
>>> for piece in furniture:
...     print(piece)
... 
...     
ottoman
sofa
table
>>> drinks = {
...     'martini':{'vodka', 'vermouth'},
...     'black russian':{'vodka', 'kahlua'},
...     'white russian':{'cream', 'kahlua', 'vodka'},
...     'manhattan':{'rye', 'vermouth', 'bitters'},
...     'screwdriver':{'orange juice', 'vodka'}
...     }
>>> for name, contents in drinks.items():
...     if 'vodka' in contents:
...         print(name)
... 
...         
martini
black russian
white russian
screwdriver
>>> for name, contents in drinks.items():
...     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
...         print(name)
... 
...         
black russian
screwdriver
>>> for name, contents in drinks.items():
...     if contents & {'vermouth', 'orange juice'}:
...         print(name)
... 
...         
martini
manhattan
screwdriver
