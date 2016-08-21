#! /usr/bin/python

def testTrue(boolString):
  trueStrings = {"true", "True", "TRUE", "T", "t"}
  result = any(boolString in trueString for trueString in trueStrings)
  print (result)
  return result
