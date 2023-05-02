import random

s = "abcdefghijklmnopqrstuvwxyz"

list = random.sample(s, len(s))   # generates random permutation

print('key = ' + '' . join(list))
