#! /usr/bin/python
import random


def shuffle(lst):
    """
    Shuffle a list
    """
    random.shuffle(lst)
    return lst


class O:
    """
    Basic Class which
        - Helps dynamic updates
        - Pretty Prints
    """

    def __init__(self, **kwargs):
        self.has().update(**kwargs)

    def has(self):
        return self.__dict__

    def update(self, **kwargs):
        self.has().update(kwargs)
        return self

    def __repr__(self):
        show = [':%s %s' % (k, self.has()[k])
                for k in sorted(self.has().keys())
                if k[0] is not "_"]
        txt = ' '.join(show)
        if len(txt) > 60:
            show = map(lambda x: '\t' + x + '\n', show)
        return '{' + ' '.join(show) + '}'


class Decision(O):
  """
  Class indicating decision of a problem
  """
  def __init__(self, name, low, high):
    """
    :param name: Name of decision
    :param low: Least value of decision
    :param high: Maximum value of decision
    """
    O.__init__(self, name=name, low=low, high=high)


class Objective(O):
  """
  Class indicating objective of a problem
  """
  def __init__(self, name, domin=True):
    """
    :param name: Name of decision
    :param domin: Want to minimize? or Maximize?
    """
    O.__init__(self, name=name, domin=domin)


class Point(O):
  """
  Class indicating a member of population
  """
  def __init__(self, decisions):
    O.__init__(self)
    self.decisions = decisions
    self.objectives = None
    self.energy = None

  def __eq__(self, other):
    return self.decisions == other.decisions


class Problem(O):
  """
  Class representing the Osyczka2 problem
  """
  def __init__(self):
    O.__init__(self)
    self.decisions = []
    self.decisions.append(Decision('x1', 0, 10))
    self.decisions.append(Decision('x2', 0, 10))
    self.decisions.append(Decision('x3', 1, 05))
    self.decisions.append(Decision('x4', 0, 06))
    self.decisions.append(Decision('x5', 1, 05))
    self.decisions.append(Decision('x6', 0, 10))
    self.objectives = [Objective('f1', True), Objective('f2', True)]
    self.points = []

  def evaluate(self, point):
    [x1, x2, x3, x4, x5, x6] = self.decisions
    f1 = -(25*((x1-2)**2) + (x2-2)**2 + (x3-1)**2 * (x4-4)**2 + (x5-1)**2)
    f2 = x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2
    point.objectives = [f1, f2]
    point.energy = f1 + f2
    return point.objectives

  @staticmethod
  def is_valid(self, point):
    """
    Check if point lies in valid range. All points valid in this case.
    :param point:
    :return: True
    """
    [x1, x2, x3, x4, x5, x6] = point.decisions
    if x1 + x2 -2 < 0: return False
    if 6 - x1 - x2 < 0: return False
    if 2 - x2 + x1 < 0: return False
    if 2 - x1 + 3*x2 < 0: return False
    if 4 - (x3 - 3)**2 - x4 < 0: return False
    if (x5 - 3)**3 + x6 - 4 < 0: return False
    return True

  def generate_one(self):
    """
    Generate a valid random point, evaluate it and add it to points list.
    :return: generated point
    """
    while True:
      mypoint = Point([random.randint(d.low, d.high) for d in self.decisions])
      if self.is_valid(mypoint):
        self.evaluate(mypoint)
        self.points.append(mypoint)
        return mypoint




class MaxWalkSat(O):
  """
  FOR i = 1 to max-tries DO
  solution = random assignment
  FOR j =1 to max-changes DO
    IF  score(solution) > threshold
        THEN  RETURN solution
    FI
    c = random part of solution
    IF    p < random()
    THEN  change a random setting in c
    ELSE  change setting in c that maximizes score(solution)
    FI
  RETURN failure, best solution found
  """
  def __init__(self, problem):
    O.__init__(self)
    self.Prob = problem()
    self.P = 0.5
    self.MAX_TRIES = 100
    self.MAX_CHANGES = 100
    self.best = self.Prob.generate_one()

  def run(self, problem):
    for i in xrange(self.MAX_TRIES):
      solution = problem.generate_one() # Generate and evaluate a new point.
      for j in xrange(self.MAX_CHANGES):
        c = random.choice(solution.decisions)


