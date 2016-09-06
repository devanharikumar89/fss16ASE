#!/usr/bin/python
from __future__ import division, print_function

class Employee(object):
  def __init__(self, name=None, age=None):
    self.name=name
    self.age=age

  def __repr__(self):
    return self.__class__.__name__+self.kv(self.__dict__)

  def kv(self, dict_):
    return '('+', '.join(['%s: %s' % (k,dict_[k]) for k in sorted(dict_.keys()) if k[0] != "_"]) + ')'

  def __cmp__(self, other):
    return self.age-other.age


E1 = Employee("Arjun", 25)
E2 = Employee("Devan", 27)
E3 = Employee("Jordy", 27)
E4 = Employee("Test", 21)
E5 = Employee("Test1", 26)

employees = [E1, E2, E3, E4, E5]
print (sorted(employees))
