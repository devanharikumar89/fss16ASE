#!/usr/bin/python
from __future__ import division
import random
import sys

def has_duplicates(list_=None):
  if type(list_) is list:
    dict_ = {}
    for item in list_:
      if item in dict_:
        return True
      else:
        dict_[item]=item
    return False
  else:
    raise ValueError("Only lists allowed\n")


def generate_birthday_list():
  list_ = []
  for _ in range(23):
    list_.append(random.randint(1,366))
  return list_

if len(sys.argv) < 2:
  print 'Usage : python <filename> <no of simulations>'
  sys.exit(0)

positive = 0
negative = 0
simulations = int(sys.argv[1])

for _ in range(simulations):
  if has_duplicates(generate_birthday_list()):
    positive += 1
  else:
    negative += 1

print positive/(positive+negative)
