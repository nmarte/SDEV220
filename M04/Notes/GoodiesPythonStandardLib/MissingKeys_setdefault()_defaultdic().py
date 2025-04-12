periodic_table = {'Hydrogen': 1, 'Helium':2}
print(periodic_table)
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)
helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)

from collections import defaultdict
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
periodic_table['Lead']

print(periodic_table)

# The argument to defaultdict() is a function that returns the value to be assigned to a missing key. 
# In the following example, no_idea() is executed to return a value when needed:
from collections import defaultdict
def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

# By the way, you can use lambda to define your default-making function right inside the call:
bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

# Using int is one way to make your own counter:
from collections import defaultdict

food_counter = defaultdict(int)

for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

# SELF MODIFIED
# Assigned list items to variable, and it works just the same
from collections import defaultdict
food_counter = defaultdict(int)
shopping_list = ['spam', 'spam', 'eggs', 'ham']
for food in shopping_list:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

# ALTERNATE VERSION
dict_counter = {}
for food in shopping_list:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items():
    print(food, count)