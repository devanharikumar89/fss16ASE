#! /usr/bin/python

from swampy.TurtleWorld import *
import math

def polygon(t,l,n,arc):
  """ Sketches a polygon of n sides each of side length l
      using turtle t. Draws as many sides as there are n*arc/360
      Use arc=360 for a full polygon, less than that for partial
      arc>360 overdraws on the sides that are already drawn
  """
  assert(n>2), 'Need atleast three sides to make a polygon'
  for i in xrange(int(n*arc/360)):
    pd(t)
    fd(t,l)
    rt(t,360.0/n)

def square(t,l):
  """ Draw a full square of length l using turtle t
  """
  polygon(t,l,4,360)

def arc(t,r,arc):
  """ Draw an arc of radius r, degree "arc" using turtle t
  """
  t.delay = 0.001
  n = int(20*math.pi*r)
  rt(t, arc/2*n)
  polygon(t,0.1,n,arc)
  lt(t, arc/2*n)

def circle(t,r):
  """ Draw an full circle of radius r using turtle t
  """
  arc(t,r,360)

def pie(t,l,n):
  """ Sketch a full pie of n sides and l length using turtle t
  """
  polygon(t,l,n,360)
  theta = (180.0-360.0/n)/2
  h = l*math.tan(theta*math.pi/180)/2
  rad = math.sqrt(h**2+(l/2.0)**2)
  print n,l,theta,h,rad
  fd(t,l/2)
  pu(t)
  for i in range(n):
    rt(t)
    fd(t,h)
    lt(t,90+theta)
    pd(t)
    fd(t,rad)
    rt(t,180)
    lt(t,theta)
    pu(t)
    fd(t,l/2)
  bk(t,l/2)

def drawPetals(t, radius, angle):
  """Draws a petal using two arcs"""
  arc(t, radius, angle)
  rt(t, 180-angle)
  arc(t, radius, angle)
  rt(t, 180-angle)

def flower(t, radius, petals, angle):
  """Draws a flower given the number of petals, angle and radius of each arc """
  for _ in xrange(petals):
    drawPetals(t, radius, angle)
    rt(t, 360/petals)
    

def exercise_4_0(bob,rad):
  """ Test the square, polygon, circle and arc functions
  """
  circle(bob,rad)
  square(bob,rad)
  polygon(bob,rad,6,360)
  arc(bob,rad,135)

def exercise_4_2(bob):
  """ General set of functions that can draw flowers
  """
  bob.delay = 0
  pu(bob)
  rt(bob)
  fd(bob, 500)
  flower(bob, 60, 7, 360/7)
  pu(bob)
  lt(bob)
  fd(bob, 200)
  flower(bob, 60, 10, 45)
  pu(bob)
  lt(bob)
  fd(bob, 200)
  flower(bob, 75, 7, 100)
  return

def exercise_4_3(bob,alice,rad):
  """ Sketch 4 pies of 4,5,6,7 sides each
  """
  bob.delay = 0.1
  alice.delay = 0.1
  pu(bob)
  fd(bob,2*rad)
  rt(bob)
  fd(bob,rad)
  pd(bob)
  pie(bob,rad,4)
  bk(bob,2*rad)
  pu(alice)
  bk(alice,0*rad)
  rt(alice)
  fd(alice,rad)
  pd(alice)
  pie(alice,rad,5)
  bk(alice,2*rad)
  pie(bob,rad,6)
  pie(alice,rad,7)

if __name__ == '__main__':
  world = TurtleWorld()
  bob = Turtle()
  alice = Turtle()
  carl = Turtle()
  rad = 80
  #exercise_4_0(bob,rad)
  exercise_4_2(carl)
  exercise_4_3(bob,alice,rad)


wait_for_user()
