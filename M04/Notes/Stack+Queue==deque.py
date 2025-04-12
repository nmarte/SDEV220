'''
Stack + Queue == deque
'''

# Function uses deque 'deck' is a double-ended queue (stack and queue).
# Useful to add and delete items from either end of a sequence.
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

# Test
print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))

'''
If you really wanted a quick palindrome checker, it would be a lot simpler 
to just compare a string with its reverse.  Python doesn’t have a reverse()
function for strings, but it does have a way to reverse a string 
with a slice, as illustrated here:
'''
def another_palindrome(word):
    return word == word[::-1] # list[<start>:<stop>:<step>]