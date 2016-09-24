#! /usr/bin/python
import sys
import collections


class Solution1(object):
  """
  Divide two integers without using multiplication, division and mod operator.
  If it is overflow, return MAX_INT.
  Remainder should be positive or negative depending on sign of divisor*dividend.
  So abs(quotient) will always be the same.
  Repeated subtraction is slow, so use long division method
  :type dividend: int
  :type divisor: int
  :rtype: int
  """
  def __init__(self):
    self.quotient = 0
    self.carry = 0
    self.divisor = 0

  def mydiv(self):  # smaller division of carry and divisor.
    result = 0
    while self.carry >= self.divisor:
      result += 1
      self.carry -= self.divisor
    if result > 0:
      self.quotient = self.quotient * 10 + result

  def shift_left(self, dividend):
    """
    Add more digits to carry until we have enough to divide in mydiv
    :param dividend:
    :return:
    """
    mylist = list(str(dividend))
    while self.carry < self.divisor and len(mylist) > 0:
      self.carry = self.carry * 10 + int(mylist.pop(0))
      if self.carry < self.divisor:
        self.quotient *= 10  # add a zero to quotient if one digit didn't pull carry above divisor
    self.mydiv()
    dividend = (0 if mylist == [] else int(''.join(mylist)))
    return dividend, len(mylist)  # return length to distinguish actual zero and empty list (end of division).

  def divide(self, dividend, divisor):

    if not divisor:
      return -1

    negate = 1 if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) else -1
    dividend, divisor = abs(dividend), abs(divisor)  # Divide like positive numbers and return minus(result) if negative
    self.quotient, self.carry, self.divisor = 0, 0, divisor
    myl = len(str(dividend))

    while dividend != 0 or myl != 0:  # myl takes care of Divident=0 but there still is 1 digit '0' to carry on division
      dividend, myl = self.shift_left(dividend)

    return min(negate * self.quotient, 2147483647)  # Max int value in c functions - 2^32 -1


class Solution2(object):
  def twoSum(self, nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    Given nums = [2, 7, 11, 15], target = 9; Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, n1 in enumerate(nums):
      for j, n2 in enumerate(nums[i+1:]):
        if n1 + n2 == target:
          return [i, i + 1 + j]



class LRUCache(object):
  def __init__(self, capacity):
    """
    :type capacity: int
    cache is list of list of 2 : key, value pair. in order of LRU
    """
    self.cache = collections.OrderedDict()  # OrderedDict remembers order in which added
    self.capacity = capacity

  def set(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: nothing
    """
    if key in self.cache:
      del self.cache[key]
    else:
      if len(self.cache) == self.capacity:
        self.cache.popitem(last=False)  # Removes the first item added to the dict, currently in the dict.
    self.cache[key] = value

  def get(self, key):
    """
    :rtype: int
    """
    if key in self.cache:
      val = self.cache.pop(key)
      # del self.cache[key]
      self.cache[key] = val
    else:
      val = -1

    return val


class Solution3(object):
  """
  Given a string, find the length of the longest substring without repeating characters.
  Given "abcabcbb", the answer is "abc", which the length is 3.
  Algorithm: Keep a longest and current list. For each char in string, keep adding to current until there is a repeat.
  In repeat, check if current greater than longest, update it. Then delete current upto char which repeats and continue.
  """
  def __init__(self):
    self.longest = []
    self.current = []

  def updatelongest(self):
    if len(self.current) > len(self.longest):
      self.longest = self.current[:]  # slice list. Or, longest will become a PTR and get affected when current changes

  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    for c in s:
      if c in self.current:
        self.updatelongest()
        del self.current[:self.current.index(c)+1]
      self.current.append(c)
    self.updatelongest()  # update one last time, lest longest will stay null if there are no repeating characters.
    return len(self.longest)


class Solution4(object):
  """
  You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
  Define a pair (u,v) which consists of one element from the first array and one element from the second array.
  Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
  Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3;  Return: [1,2],[1,4],[1,6]
  """
  def __init__(self):
    self.nums1, self.nums2 = 0, 0
    self.returnList = []
    self.iterators = []  # One iterator for each element of first array,
    # that points to which element in nums2 has to be considered next

  def get_next_iter(self):
    # mysum = -sys.maxsize-1  # There is one more negative numbers than positive
    mysum = sys.maxsize
    myi, myj = -1, -1
    for i, j in enumerate(self.iterators):
      if j < len(self.nums2):
        if self.nums1[i] + self.nums2[j] < mysum:
          myi, myj, mysum = i, j, self.nums1[i] + self.nums2[j]

    self.iterators[myi] += 1  # mark as used
    assert -1 < myi < len(self.nums1) and -1 < myj < len(self.nums2)
    return myi, myj

  def kSmallestPairs(self, nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    self.nums1, self.nums2 = nums1, nums2
    self.iterators = [0 for _ in xrange(len(nums1))]
    for _ in xrange(min(k, len(nums1)*len(nums2))):
      i, j = self.get_next_iter()
      self.returnList.append([nums1[i], nums2[j]])
    return self.returnList

# s = Solution4()
# print s.kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 20)

