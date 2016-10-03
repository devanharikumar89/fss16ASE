#! /usr/bin/python

from string import whitespace
import random

def countdown(n):
  while n >= 0:
    yield n
    n -= 1


def items(x, depth=-1):
  if isinstance(x,(list,tuple)):
    for y in x:
      # yield [z for z in items(y, depth+1) if z > 20]
       for z in items(y, depth+1):
        if z > 20:
          yield z
  else:
    yield x

out = []
for x in items([10, [20, 30],
                        40,
                        [(50, 60, 70),
                            [80, 90, 100], 110]]):
   out += [x]
print out

def nonwhtspc (mystr):
  newstr = ''
  for c in mystr:
    if c not in whitespace:
      newstr += c
  print newstr


def randodd (myrange):
  # while True:
  return random.randrange(1, myrange, 2)



somestr = "We are go for\tlaunch\t"
print(somestr)
for x in countdown(10):
  print(x)
print("lift off!")
nonwhtspc(somestr)

x = []
# random.seed(1)
for _ in range(20):
  x.append(random.random())
  print randodd(1000)
print(x)


class Solution(object):
  def is_valid(self, mystr):
    """
    :type mystr: str
    :rtype: bool
    """
    mylist = []
    for c in mystr:
      if c in ['(', '{', '[']:
        mylist.append(c)
      else:
        if len(mylist) == 0:
          return False
        if mylist[-1] == '(' and c != ')':
          return False
        if mylist[-1] == '{' and c != '}':
          return False
        if mylist[-1] == '[' and c != ']':
          return False
        del (mylist[-1])
    return mylist == []

s = Solution()
print s.is_valid("({[]}))")
print 22/-3