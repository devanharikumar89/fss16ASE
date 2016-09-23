from __future__ import print_function
from __future__ import division
import schaffer
import random


def say(x):
  print(x, end="")


class Sa(object):

  def start_annealing(self, f):
    s = f.get_rand_value() #initial state
    e = f.norm_energy(s) #initial energy
    sb, eb = s, e #set best state and best energy to initial values
    kmax, kmin = 10000, 1 #max and min temp
    self.new_line(sb, eb)
    while kmin < kmax and e > f.get_emax(): #stops when temp is max or we reach enough energy
      if kmin % 25 == 0:
        self.new_line(sb, eb)

      sn = f.get_neighbour(s) #new state
      en = f.norm_energy(sn) #new energy
      if en < eb: #if new state and energy is better set best state and best energy to ner values
        sb, eb = sn, en
        say("!")
      # if new state and energy is better set current state and best energy to ner values
      # if new state and energy is worse let the probability function decide
      # at lower temperature there is a higher probability that
      # current state and best energy to ner values is set to new state and energy
      if en < e:
        s, e = sn, en
        say("+")
      elif f.probability(e, en, kmin/kmax) < random.random():
        s, e = sn, en
        say("?")

      say(".")
      kmin += 1
    return sb, eb


  def new_line(self, sb, eb):
    """
    Pretty printing
    :param sb: best solution
    :param eb: best energy
    :return: None
    """
    say("\nsb: ")
    say(sb)
    say(" eb: ")
    say(eb)
    say(" ")

epsilon = 0.9999999 #emax is maximum energy - epsilon
schaffer = schaffer.Schaffer(epsilon)
schaffer.set_baseline(1000)

sa = Sa()
sb, eb = sa.start_annealing(schaffer)
sa.new_line(sb, eb)
say("\n")
