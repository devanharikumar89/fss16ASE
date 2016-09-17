from __future__ import division
import random
import math

class Schaffer(object):

  def __init__(self, epsilon):
    self.x_low = -1 * 10 ** 5
    self.x_high = 1 * 10 ** 5
    self.min_e = Schaffer.energy(self.x_high)
    self.max_e = Schaffer.energy(0)
    self.epsilon = epsilon

  @staticmethod
  def f1(x):
    """
    -10^5 <= x <= 10^5
    :param x:
    :return: x^2
    """
    return x ** 2

  @staticmethod
  def f2(x):
    """
    -10^5 <= x <= 10^5
    :param x:
    :return: (x - 2)^2
    """
    return (x - 2) ** 2

  @staticmethod
  def energy(x):
    return Schaffer.f1(x) + Schaffer.f2(x)

  def get_rand_value(self):
    return round(random.uniform(self.x_low, self.x_high), 2)

  def get_neighbour(self, x, r=1000):
    if x - r < self.x_low and x + r > self.x_high: return self.get_rand_value()
    elif x - r < self.x_low: return round(random.uniform(self.x_low, x + r), 2)
    elif x + r >  self.x_high: return round(random.uniform(x - r, self.x_high), 2)
    return round(random.uniform(x - r, x + r), 2)

  def set_baseline(self, n_times):
    for _ in xrange(n_times):
      r_val = self.get_rand_value()
      e = Schaffer.energy(r_val)
      if e < self.min_e: self.min_e = e
      if e > self.max_e: self.max_e = e

  def norm_energy(self, x):
    return (Schaffer.energy(x) - self.min_e) / (self.max_e - self.min_e)

  def get_emax(self):
    return 1 - self.epsilon

  def probability(self, e, en, t):
    var = (e - en) / t
    return math.exp(var)
