from __future__ import print_function
from __future__ import division
import schaffer
import random

def say(x):
  print(x, end="")

class Sa(object):


  def start_annealing(self, f):
    s = f.get_rand_value()
    e = f.norm_energy(s)
    sb, eb = s, e
    kmax, kmin = 10000, 1
    self.new_line(sb, eb)
    while kmin < kmax and e > f.get_emax():
      if kmin % 25 == 0:
        self.new_line(sb, eb)

      sn = f.get_neighbour(s)
      en = f.norm_energy(sn)
      if en < eb:
        sb, eb = sn, en
        say("!")

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
    say("\nsb: ")
    say(sb)
    say(" eb: ")
    say(eb)
    say(" ")

epsilon = 0.9999999
schaffer = schaffer.Schaffer(epsilon)
schaffer.set_baseline(1000)

sa = Sa()
sb, eb = sa.start_annealing(schaffer)
sa.new_line(sb, eb)
say("\n")
