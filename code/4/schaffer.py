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
    :param x: float -10^5 <= x <= 10^5
    :return: float x^2
    """
    return x ** 2

  @staticmethod
  def f2(x):
    """
    :param x: float -10^5 <= x <= 10^5
    :return: float (x - 2)^2
    """
    return (x - 2) ** 2

  @staticmethod
  def energy(x):
    """
    Calculates the energy for x val
    :param x: float -10^5 <= x <= 10^5
    :return: float f1(x) + f2(x)
    """
    return Schaffer.f1(x) + Schaffer.f2(x)

  def get_rand_value(self):
    """
    :return: float a random value between -10^5 and 10^5
    """
    return round(random.uniform(self.x_low, self.x_high), 2)

  def get_neighbour(self, x, r=1000):
    """
    gets a random neighbour value of x within the range of r,
    however, this neighbour value cannot be less than -10^5
    or greater than 10^5
    :param x: float -10^5 <= x <= 10^5
    :param r: int default 1000
    :return: float random neighbour value of x within the range of r
    """
    if x - r < self.x_low and x + r > self.x_high: return self.get_rand_value()
    elif x - r < self.x_low: return round(random.uniform(self.x_low, x + r), 2)
    elif x + r >  self.x_high: return round(random.uniform(x - r, self.x_high), 2)
    return round(random.uniform(x - r, x + r), 2)

  def set_baseline(self, n_times):
    """
    sets the baseline minimum energy and maximum energy
    :param n_times: int Number of samples to consider to set baseline values
    :return: None
    """
    for _ in xrange(n_times):
      r_val = self.get_rand_value()
      e = Schaffer.energy(r_val)
      if e < self.min_e: self.min_e = e
      if e > self.max_e: self.max_e = e

  def norm_energy(self, x):
    """
    Normalize energy for x
    :param x: float -10^5 <= x <= 10^5
    :return: Normalized energy
    """
    return (Schaffer.energy(x) - self.min_e) / (self.max_e - self.min_e)

  def get_emax(self):
    """
    get enough energy, normally it is maximum energy minus the epsilon
    :return:
    """
    return 1 - self.epsilon

  def probability(self, e, en, t):
    """
    probability function
    :param e: current energy
    :param en: new energy
    :param t: temperature
    :return:e^ ((e-en)/t)
    """
    var = (e - en) / t
    return math.exp(var)
