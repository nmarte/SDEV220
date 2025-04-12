Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def menu(wine, entree, dessert='pudding'):
...     return {'wine':wine, 'entree':entree, 'dessert':dessert}
... 
>>> menu('chardonnay', 'chicken')
{'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}
>>> menu('dunkelfelder', 'duck', 'doughnut')
{'wine': 'dunkelfelder', 'entree': 'duck', 'dessert': 'doughnut'}
>>> 
>>> 
>>> def buggy(arg, result=[]):
...     result.append(arg)
...     print(result)
... 
...     
>>> buggy('a')
['a']
>>> buggy('b')
['a', 'b']
>>> 
>>> # alternatively
>>> def works(arg):
...     result = []
...     result.append(arg)
...     return result
... 
>>> works('a')
['a']
>>> works('b')
['b']
>>> buggy('c')
['a', 'b', 'c']
