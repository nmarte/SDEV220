Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print('\tac')
	ac
print('\tabc')
	abc
print('a\tbc')
a	bc
print('ab\tc')
ab	c
print('abc
      
SyntaxError: unterminated string literal (detected at line 1)
print('abc\t')
      
abc	
testimony = '\"I did nothing!\" he said. \"or that other thing.\""
      
SyntaxError: unterminated string literal (detected at line 1)
testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
      
testimony
      
'"I did nothing!" he said. "Or that other thing."'
print(testimony)
      
"I did nothing!" he said. "Or that other thing."
>>> speech = 'The backlash (\\) bends over backwards to please you.'
...       
>>> print(speech)
...       
The backlash (\) bends over backwards to please you.
>>> speech_1 = 'The backslash (\) bends over backwards to please you.'
>>> speech_1
'The backslash (\\) bends over backwards to please you.'
>>> print(speech_1)
The backslash (\) bends over backwards to please you.
>>> poem = r'''Boys and girls, come out to play.
... The moon doth shine as bright as day.'''
>>> poem
'Boys and girls, come out to play.\nThe moon doth shine as bright as day.'
>>> print(poem)
Boys and girls, come out to play.
The moon doth shine as bright as day.
>>> 'Release the kraken!' + 'No, wait!'
'Release the kraken!No, wait!'
>>> 'Release the kraken!' +
SyntaxError: invalid syntax
>>> start = 'Na ' * 4 + '\n'
>>> midle = 'Hey ' *3 + '\n'
>>> end = 'Goodbye.'
>>> print(start + start + middle + end)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(start + start + middle + end)
NameError: name 'middle' is not defined. Did you mean: 'midle'?
>>> print(start + start + midle + end)
Na Na Na Na 
Na Na Na Na 
Hey Hey Hey 
Goodbye.
>>> name = 'Henny'
>>> name.replace('H', 'P')
'Penny'
>>> 'P' + name[1:]
'Penny'
