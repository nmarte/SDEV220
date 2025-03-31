Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Henny'
name.replace('H', 'P')
'Penny'
name
'Henny'
'P' + name[1:]
'Penny'
name
'Henny'
letters = 'abcdefghijklmnopqrstuvwxyz'
letters[:]
'abcdefghijklmnopqrstuvwxyz'
letters[20:]
'uvwxyz'
letters[10]
'k'
letters[10:]
'klmnopqrstuvwxyz'
letters[-1::-1]
'zyxwvutsrqponmlkjihgfedcba'
tasks = 'get gloves, get mask, give cat vitamins, call ambulance'
tasks.split(',')
['get gloves', ' get mask', ' give cat vitamins', ' call ambulance']
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
ctypto_list = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print('Found and signing book deals:', crypto_string)
NameError: name 'crypto_string' is not defined
crypto_list = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print('Found and signing book deals:', crypto_string)
NameError: name 'crypto_string' is not defined
>>> setup = "a duck goes into a bar..."
>>> setup.replace('duck', 'marmoset')
'a marmoset goes into a bar...'
>>> setup
'a duck goes into a bar...'
>>> setup.replace('a ', 'a famous ', 100)
'a famous duck goes into a famous bar...'
>>> world = "    earth    "
>>> world.strip()
'earth'
>>> world.strip(' ')
'earth'
>>> world.lstrip()
'earth    '
>>> world.rstrip()
'    earth'
>>> blurt = "What the...!!?"
>>> blurt.strip('.?!')
'What the'
>>> import string
>>> string.whitespace
' \t\n\r\x0b\x0c'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> blurt = "What the...!!?"
>>> blurt.strip(punctuation)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    blurt.strip(punctuation)
NameError: name 'punctuation' is not defined
>>> blurt.strip(string.punctuation)
'What the'
>>> prospector = "What in tarnation ...??!!"
>>> prospector.strip(string.whitespace + string.punctuation)
'What in tarnation'
