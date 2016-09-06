#! /usr/bin/python
import random

"""
quot, rem = divmod(7, 3)
A parameter name that begins with * gathers arguments into a tuple
s, t = 'abc', [0, 1, 2]  >>> zip(s, t):  [('a', 0), ('b', 1), ('c', 2)]
t = [('a', 0), ('c', 2), ('b', 1)]   >>> d = dict(t) makes a dict out of the tuple
Tuples are immutable, no methods like sort and reverse, which modify existing lists. But has sorted and reversed, which return a new list with the same elements in a different order.
sentence = ['this','is','a','sentence']  >>> '-'.join(sentence) : 'this-is-a-sentence'
list = string.split()
The string module provides strings named whitespace, which contains space, tab, newline, etc.
print string.punctuation : !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

"""





def print_nest_list(a):
  # noinspection PyBroadException
  print "Print_net_list"
  try:
    for e in a:
      for x in e:
        print x,
      print ""
    print ""
  except:
    print "Empty list passed"
  return


def nested_sum(a, sum_list=False):
  my_sum = 0
  for (ne, e) in enumerate(a):
    for (nx, x) in enumerate(e):
      try:
        my_sum += x
        a[ne][nx] = my_sum if sum_list else x
      except TypeError:
        print "List element \"", x, '" at position [', ne, ',', nx, '] skipped as it is not a number'
  print "Cumulative Sum:", my_sum
  if sum_list:
    print_nest_list(a)
  return


def capitalize_all(t):
  res = []
  for s in t:
    try:
      res.append(s.capitalize())
    except AttributeError:
      print "Skipping element since its not a string"
  return res


def cap_nested(t):
  res = []
  for s in t:
    res.append(capitalize_all(s))
  return res


def middle(a):
  res = a[1:-2] if len(a) > 2 else []
  print "My print", len(a)
  print_nest_list(res)
  print "My print"
  print_nest_list(a)
  return


def chop(a):
  length = len(a)
  if length > 0:
    del a[0]
  if length > 0:
    del a[-1]
  return None


def is_sorted(my_list):
  for i in xrange(len(my_list)-1):
    # try:
    #   int(my_list[i])
    # except ValueError:
    #   return False
    if my_list[i] >= my_list[i+1]:
      return False
  return True


def is_anagram(one, two):
  return sorted(one) == sorted(two)


def has_duplicates(list_in):
  my_list = sorted(list_in)
  for i in xrange(len(my_list)-1):
    if my_list[i] == my_list[i+1]:
      return True
  return False


def birthday_paradox(class_size, poll_size):
  prob = 0.0
  for _ in xrange(poll_size):
    prob += float(has_duplicates([random.randrange(365) for _ in xrange(class_size)]))/poll_size
  print prob


def histogram(s):
  d = {}
  for c in s:
    d[c] = d.get(c, 0) + 1
  return d


def invert_dict(d):
  inv = dict()
  for c in d:
    val = d[c]
    inv[val] = (inv.setdefault(val, []))
    inv[val].append(c)
  return inv


def fib(n, known={0:0, 1:1}):
  if n in known:
    return known[n]
  else:
    value = fib(n-1) + fib(n-2)
    known[n] = value
  return value


def length_sort(lt):
  res, tl = [], []
  for word in lt:
    tl.append((len(word), random.random(), word))
  tl.sort(reverse=True)
  for len_word, rand, word in tl:
    res.append(word)
  return res


def most_frequent(st):
  lt = invert_dict(histogram(st))
  print lt
  for k in lt.keys():
    print k, ': ',
    for c in lt[k]:
      print c,
    print ""
  return None

l = [[1, 2, 'zebra'], [4, 3, 'a', 5], [1]]
word_s = 'The quick brown fox jumped over the lazy dog'
word_l = word_s.split()
words = ''.join(word_l)
# nested_sum(l, False)
# print cap_nested(l)
# middle(l)
# chop(l)
# print_nest_list(l)
# print(is_sorted([1, 2, 1]))
# print(is_sorted([1, 2, 'A', 'b', 'c']))
# print(is_anagram('abba', 'aabb'))
# print has_duplicates([1, 2, 3, 5, 4, 8, 6, 7, 9, 0, 'a', 4])
birthday_paradox(23, 1500)
print(invert_dict(histogram('abracadabra')))
print fib(32)
print length_sort(word_l)
print most_frequent(words)
