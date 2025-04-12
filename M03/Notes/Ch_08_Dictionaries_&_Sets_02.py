Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
drinks = {
    'martini':{'vodak', 'vermouth'},
    'black russian':{'vodka', 'kahlua'},
    'white russian':{'cream', 'kahlua', 'vodka'},
    'manhattan':{'rye', 'vermouth', 'bitters'},
    'screwdriver':{'orange juice', 'vodka'}
    }
for name, contents in drinks.items)_:
    
SyntaxError: unmatched ')'
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

        
black russian
white russian
screwdriver
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

        
black russian
white russian
screwdriver
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or
                                    'cream' in contents):
        print(name)

        
black russian
screwdriver
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

        
martini
manhattan
screwdriver
for name contents in drinks.items():
    
SyntaxError: invalid syntax
# must have comma
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

        
black russian
screwdriver
bruss = drinks['black russian']
wruss = drinks['white russian']
a = {1,2}
b = {2,3}
a & b
{2}
a.intersection(b)
{2}
bruss & wruss
{'kahlua', 'vodka'}
a | b
{1, 2, 3}
a.union(b)
{1, 2, 3}
bruss | wruss
{'vodka', 'cream', 'kahlua'}
a - b
{1}
a.difference(b)
{1}
bruss - wruss
set()
wruss - bruss
{'cream'}
a ^ b
{1, 3}
a.symmetric_difference(b)
{1, 3}
bruss ^ wruss
{'cream'}
a <= b
False
a.issubset(b)
False
bruss <= wruss
True
a <= a
True
a.issubset(a)
True
a < b
False
a < a
False
bruss < wruss
True
a >= b
False
a.issuperset(b)
False
wruss >= bruss
True
bruss >= wruss
False
a_set = {number for number in range(1,6) if number % 3 == 1}
a_set
{1, 4}
frozenset([3,2,1])
frozenset({1, 2, 3})
frozenset(set([2,1,3]))
frozenset({1, 2, 3})
frozenset({3,1,2})
frozenset({1, 2, 3})
frozenset((2,3,1))
frozenset({1, 2, 3})
fs = frozenset([3,2,1])
fs
frozenset({1, 2, 3})
fs.add(4)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    fs.add(4)
AttributeError: 'frozenset' object has no attribute 'add'
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho':'banjo', 'Chico':'piano', 'Harpo':'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}
marx_list[2]
'Harpo'
marx_tuple[2]
'Harpo'
marx_dict['Harpo']
'harp'
'Harpo' in marx_list
True
>>> 'Harpo' in marx_tuple
True
>>> 'Harpo' in marx_dict
True
>>> 'Harpo' in marx_set
True
>>> marxes = ['Groucho', 'Chico', 'Harpo']
>>> pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
>>> stooges = ['Moe', 'Curly', 'Larry']
>>> tuple_of_lists = marxes, pythons, stooges
>>> tuple_of_lists
(['Groucho', 'Chico', 'Harpo'], ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], ['Moe', 'Curly', 'Larry'])
>>> list_of_lists = [marxes, pythons, stooges]
>>> list_of_lists
[['Groucho', 'Chico', 'Harpo'], ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], ['Moe', 'Curly', 'Larry']]
>>> dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges':stooges}
>>> dict_or_lists
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    dict_or_lists
NameError: name 'dict_or_lists' is not defined. Did you mean: 'dict_of_lists'?
>>> dict_of_lists
{'Marxes': ['Groucho', 'Chico', 'Harpo'], 'Pythons': ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], 'Stooges': ['Moe', 'Curly', 'Larry']}
>>> house = {
...     (44.79, -93.14, 285): 'My House",
...     
SyntaxError: unterminated string literal (detected at line 2)
>>> houses = {
...     (44.79, -93.14, 285): 'My House',
...     (38.89, -77.03, 13):'The White House'
...     }
...     
>>> houses
...     
{(44.79, -93.14, 285): 'My House', (38.89, -77.03, 13): 'The White House'}
