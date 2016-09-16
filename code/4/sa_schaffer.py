#! /usr/bin/python
import sys, math, random

global maxim, minim, emax, xmax


def f1(x):
  return pow(x, 2)


def f2(x):
  return pow((x-2), 2)


def f(x):
  return f1(x)+f2(x)


def E(x):
  """
  :param x:
  :return: Energy of x
  """
  return (float(f(x)) - f(minim)) / (f(maxim) - f(minim))


def neighbor(x):
  """
  :param x:
  :return: x+1 or x-1 based on a random number, or based on if x is already borderline.
  """
  # print 'neighbor', x
  if abs(x) == xmax:
    return x - x/abs(x)
  return x + 1 if random.randint(0, 1) else x - 1


def prob(old, new, t):
  # return math.e ** ((old - new) / (t + 0.001))
  return 0.9


def run_init():
  global maxim, minim
  maxim, minim = 0, 0
  for _ in xrange(200):
    x = random.randrange(-xmax, xmax)
    if f(x) > f(maxim):
      maxim = x
    if f(x) < f(minim):
      minim = x
  print maxim, f(maxim), E(maxim), minim, f(minim), E(minim)


def run_sa():
  x, k, kmax = 0, 1, 1000
  e = E(x)
  xb, eb = x, e
  global emax
  emax = E(minim) - 0.002
  print ',', repr(k).rjust(3), repr(e).rjust(23), repr(float(k) / kmax).ljust(5),
  while k < kmax and e > emax:
    xn = neighbor(x)
    en = E(xn)
    if en < eb:         # New Best
      xb, eb = xn, en
      print '!',
    if en < e:          # Jump to better
      x, e = xn, en
      print '+',
    elif random.random() > prob(e, en, float(k)/kmax):  # Jump to worse
      x, e = xn, en
      print '?',
    else:
      print '.',
    k += 1
    if not k % 25 and k != 1000:
      print ""
      print ',', repr(k).rjust(3), repr(e).rjust(23), repr(float(k) / kmax).ljust(5),
  print ""
  return xb


xmax = pow(10,5)
run_init()
myx = run_sa()
print myx, f(myx), E(myx)
