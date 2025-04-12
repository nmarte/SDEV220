import itertools
for item in itertools.chain([1,2], ['a', 'b']):
    print(item)

# accumulate() calculates accumulated values. 
# By default, it calculates the sum:
import itertools
for item in itertools.accumulate([1,2,3,4]):
    print(item)

'''
You can provide a function as the second argument to accumulate(), 
and it will be used instead of addition. The function should take two 
arguments and return a single result. This example calculates an 
accumulated product:
'''
# import itertools # redundant due to previous imports
def multiply(a,b):
    return a * b

for item in itertools.accumulate([1,2,3,4], multiply):
    print(item)