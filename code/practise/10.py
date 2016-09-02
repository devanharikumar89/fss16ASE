#! /usr/bin/python


def print_nest_list(a):
  # noinspection PyBroadException
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
    except TypeError:
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
  if len(a) < 3:
    a = []
  else:
    del a[0]
    del a[-1]

  return None

l = [[1, 2, 'zebra'], [4, 3, 'a', 5]]
nested_sum(l, True)
print cap_nested(l)
middle(l)
chop(l)
print_nest_list(l)
