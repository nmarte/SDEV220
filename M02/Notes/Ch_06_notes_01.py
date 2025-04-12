Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
count = 1
while couht <= 5:
    print(count)
    count += 1

    
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    while couht <= 5:
NameError: name 'couht' is not defined. Did you mean: 'count'?
count = 1
while count <= 5:
    print(count)
    count += 1

    
1
2
3
4
5
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

    
String to capitalize [type q to quit]: test
Test
String to capitalize [type q to quit]: hey, it works
Hey, it works
String to capitalize [type q to quit]: q
while True:
    value = input("integer, please [q to quit]: ")
    if value == "q": # quit
        break
    number = int(value)
    if number % 2 == 0: # an even number
        continue
    print(number, "squared is", number*number)

    
integer, please [q to quit]: 1
1 squared is 1
integer, please [q to quit]: 2
integer, please [q to quit]: 3
3 squared is 9
integer, please [q to quit]: 4
integer, please [q to quit]: 5
5 squared is 25
integer, please [q to quit]: q
numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else: # break not called
    print('no even number found')

    
no even number found
word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1
... 
...     
t
h
u
d
>>> # better way
>>> for letter in word:
...     print(letter)
... 
...     
t
h
u
d
>>> word = 'thud'
>>> for letter in word:
...     if letter == 'u':
...         break
...     print(letter)
... 
...     
t
h
>>> word = 'thud'
>>> for letter in word:
...     if letter == 'x':
...         print("Eek! An 'x'!")
...         break
...     print(letter)
... else:
...     print("No 'x' in there.")
... 
...     
t
h
u
d
No 'x' in there.
