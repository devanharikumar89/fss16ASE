#! /usr/bin/python

def testTrue(boolString):
  trueStrings = {"true", "True", "TRUE", "T", "t"}
  result = any(boolString in trueString for trueString in trueStrings)
  result = boolString in trueStrings 
  print ("Input string: " + boolString + "\t Result: " + str(result))
  return result
