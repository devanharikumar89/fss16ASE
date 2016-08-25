### Trick 1
#### 
Instead of doing:

i = 0 
for item in iterable: 
    print i, item 
    i += 1
We can do:

for i, item in enumerate(iterable):
    print i, item

>>> list(enumerate('abc')) 
[(0, 'a'), (1, 'b'), (2, 'c')] 

>>> list(enumerate('abc', 1)) 
[(1, 'a'), (2, 'b'), (3, 'c')]

### Trick 2
####
Dict and Set too can have comprehensions

my_dict = {i: i * i for i in xrange(100)} 
my_set = {i * 15 for i in xrange(100)}

### Trick 3
####
Forcing float division:

If we divide whole numbers Python gives us the result as a whole number even if the result was a float. 
In order to circumvent this issue we have to do something like this:

result = 1.0/2

Professor's way:

from __future__ import division 
result = 1/2

print(result)
Ans : 0.5
