Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> disaster = True
>>> if disaster:
...     print("Woe!")
... else:
...     print("Whee!")
... 
...     
Woe!
>>> furry = True
>>> large = True
>>> if furry:
...     if large:
...         print("it's a yeti.")
...     else:
...         print("Its a cat!")
... else:
...     if large:
...         print("it's a whale!")
...     else:
...         print("It's a human. Or a hairless cat.")
... 
...         
it's a yeti.
>>> 
>>> color = "mauve"
>>> if color == "red":
...     print("It's a tomato.")
... elif color == "green":
...     print("It's a green pepper")
... elif color == "bee purple":
...     print("I don't know what it is, but only bees can see it.")
... else:
...     print("I've never heard of the color", color)
... 
...     
I've never heard of the color mauve
