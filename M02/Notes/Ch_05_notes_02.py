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
speech = 'The backlash (\\) bends over backwards to please you.'
      
print(speech)
      
The backlash (\) bends over backwards to please you.
speech_1 = 'The backslash (\) bends over backwards to please you.'
speech_1
'The backslash (\\) bends over backwards to please you.'
print(speech_1)
The backslash (\) bends over backwards to please you.
poem = r'''Boys and girls, come out to play.
The moon doth shine as bright as day.'''
poem
'Boys and girls, come out to play.\nThe moon doth shine as bright as day.'
print(poem)
Boys and girls, come out to play.
The moon doth shine as bright as day.
'Release the kraken!' + 'No, wait!'
'Release the kraken!No, wait!'
'Release the kraken!' +
SyntaxError: invalid syntax
start = 'Na ' * 4 + '\n'
midle = 'Hey ' *3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(start + start + middle + end)
NameError: name 'middle' is not defined. Did you mean: 'midle'?
print(start + start + midle + end)
Na Na Na Na 
Na Na Na Na 
Hey Hey Hey 
Goodbye.
name = 'Henny'
name.replace('H', 'P')
'Penny'
'P' + name[1:]
'Penny'
'%d%%'% 100
'100%'
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
"My wife's favorite actor is %s" % actor
"My wife's favorite actor is Richard Gere"
"Our cat %s weights %s pounds" % (cat, weight)
'Our cat Chester weights 28 pounds'
thing = 'woodchuck'
'%s' % thing
'woodchuck'
'%12s' % thing
'   woodchuck'
'-12%s' % thing
'-12woodchuck'

'%+12s' % thing
'   woodchuck'
'%-12s' % thing
'woodchuck   '
'%.3s' % thing
'woo'
'%12.3s' % thing
'         woo'
'%-12.3s' % thing
'woo         '
thing = 98.6
'%f' % thing
'98.600000'
'%12f' % thing
'   98.600000'
'%+12f' % thing
'  +98.600000'
'%-12f' % thing
'98.600000   '
'%.3f' % thing
'98.600'
'%12.3f' % thing
'      98.600'
'%-12.3f' % thing
'98.600      '
'{}'.format(thing)
'98.6'
thing = 'woodchuck'
'{}'.format(thing)
'woodchuck'
place = 'lake'
'The {} is in the {}'.format(thing,place)
'The woodchuck is in the lake'
'The {1} is in the {0}'.format(place,thing)
'The woodchuck is in the lake'
>>> 'The{0} is in the {1}'.format(place,thing)
'Thelake is in the woodchuck'
>>> 'Thelake is in the woodchuck'
'Thelake is in the woodchuck'
>>> 'The {thing} is in the {place}.format(thing='duck', place='bathrub')
SyntaxError: unterminated string literal (detected at line 1)
>>> 'The {thing} is in the {place}'.format(thing = 'duck', place = 'bathrub')
'The duck is in the bathrub'
>>> d = {'thing':'duck', 'place':'bathtub'}
>>> 'The {0[thing]} is in the {0[place]}.'.format(d)
'The duck is in the bathtub.'
>>> 'The duck is in the bathtub.'
'The duck is in the bathtub.'
>>> thing = 'wraith'
>>> place = 'window'
>>> 'The {} is at the {}'.format(thing, place)
'The wraith is at the window'
>>> 'The {:10s} is at the {:10s}'.format(thing, place)
'The wraith     is at the window    '
>>> 'The {:^10s} is at the {:^10s}'.format(thing, place)
'The   wraith   is at the   window  '
>>> 'The {:!^10s} is at the {:!^10s}'.format(thing, place)
'The !!wraith!! is at the !!window!!'
>>> thing = 'wereduck'
>>> place = 'werepond'
>>> f'The {thing} is in the {place}'
'The wereduck is in the werepond'
>>> f'The {thing.capitalize()} is in the {place.rjust(20)}'
'The Wereduck is in the             werepond'
>>> f'The {thing:>20} is in the place {place:.^20}'
'The             wereduck is in the place ......werepond......'
>>> f'{thing =}, {place =}'
"thing ='wereduck', place ='werepond'"
>>> f'{thing[-4:] =}, {place.title() =}
SyntaxError: unterminated f-string literal (detected at line 1)
>>> f'{thing[-4:] =}, {place.title() =}'
"thing[-4:] ='duck', place.title() ='Werepond'"
>>> f'{thing = :>4.4}'
'thing = were'
