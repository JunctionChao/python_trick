#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-09
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# list trick

# all_equal
# Check if all elements in a list are equal.
# Use [1:] and [:-1] to compare all the values in the given list.

def all_equal(lst):
  return lst[1:] == lst[:-1]

# all_unique
# Returns True if all the values in a flat list are unique, False otherwise.
# Use set() on the given list to remove duplicates, compare its length with the length of the list.

def all_unique(lst):
  return len(lst) == len(set(lst))


# count_by
# Groups the elements of a list based on the given function and returns the count of elements in each group.

def count_by(arr, fn=lambda x: x):
  key = {}
  for el in map(fn, arr):
    key[el] = 1 if el not in key else key[el] + 1
  return key

from math import floor
count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}


# difference
# Returns the difference between two iterables.

def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]


# every
# Returns True if the provided function returns True for every element in the list, False otherwise.
def every(lst, fn=lambda x: x):
  return all(map(fn, lst))

# Examples
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True


# filter_non_unique
# Filters out the non-unique values in a list.
# Use list comprehension and list.count() to create a list containing only the unique values.

def filter_non_unique(lst):
  return [item for item in lst if lst.count(item) == 1]

filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]


# filter_unique
# Filters out the unique values in a list.
# Use list comprehension and list.count() to create a list containing only the non-unique values.

def filter_unique(lst):
  return [x for x in set(item for item in lst if lst.count(item) > 1)]


# intersection
# Returns a list of elements that exist in both lists.
# Create a set from a and b, then use the built-in set operator & to only keep values contained in both sets, 
# then transform the set back into a list.
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)

intersection([1, 2, 3], [4, 3, 2]) # [2, 3]


# max_n
# Returns the n maximum elements from the provided list. If n is greater than or equal to the provided list's length, then return the original list (sorted in descending order).
# Use sorted() to sort the list, [:n] to get the specified number of elements. Omit the second argument, n, to get a one-element list.

def max_n(lst, n=1):
  return sorted(lst, reverse=True)[:n]


# min_n
def min_n(lst, n=1):
  return sorted(lst, reverse=False)[:n]


# shuffle
# Randomizes the order of the values of an list, returning a new list.
# Uses the Fisher-Yates algorithm to reorder the elements of the list.
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst

# Examples
foo = [1,2,3]
shuffle(foo) # [2,3,1] , foo = [1,2,3]


# symmetric_difference
# Returns the symmetric difference between two iterables, without filtering out duplicate values.

# Create a set from each list, then use list comprehension on each one to only keep values not contained in the previously created set of the other.

def symmetric_difference(a, b):
  _a, _b = set(a), set(b)
  return [item for item in a if item not in _b] + [item for item in b if item not in _a]

# Examples
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]



