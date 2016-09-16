#! /usr/bin/python

import sys, __future__

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

def print_lyrics():
  print "I'm a lumberjack, and I'm okay."
  print "I sleep all night and I work all day."

def right_justify(string):
  assert(len(string)<=70)
  print(' '*(70-len(string))+string)

def do_twice(f,val=None):
  if val:
    f(val)
    f(val)
  else:
    f()
    f()

def do_four(f,val=None):
  if val:
    do_twice(f,val)
    do_twice(f,val)
  else:
    do_twice(f)
    do_twice(f)

def print_twice(val):
  print(val)
  print(val)

def print_top():
  print('+ - - - - '),

def print_mid():
  print('/         '),

def print_topline(columns):
  for i in xrange(columns):
    print_top()
  print('+')

def print_midline(columns):
  for i in xrange(columns):
    print_mid()
  print('/')

def print_row(columns):
  print_topline(columns)
  do_four(print_midline,columns)

def print_twoByTwo():
  do_twice(print_row,2)
  print_topline(2)

def print_fourByFour():
  do_four(print_row,4)
  print_topline(4)

repeat_lyrics()
right_justify("Sample String")
do_twice(print_twice,'spam')
print
do_four(print_twice,'spam')
print
print_twoByTwo()
print
print_fourByFour()
