Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> vowels = 'aeiou'
>>> letter = 'o'
>>> letter in vowels
True
>>> if letter in vowels"
SyntaxError: unterminated string literal (detected at line 1)
>>> if letter in vowels:
...     print(letter, 'is a vowel')
... 
...     
o is a vowel
