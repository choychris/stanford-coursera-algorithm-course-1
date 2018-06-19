from random import choice

a = [1, 2, 3]
dictList = {'a': a, 'b': [10,9]}
dictList['b'] = dictList['a'] + dictList['b']

for i in range(20):
  print (choice(dictList['b']))

