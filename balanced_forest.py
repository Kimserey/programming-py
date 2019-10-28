import math
import os
import random
import re
import sys
import copy

# Compute total for a given root and set of edges.
# In : computeTotal(1, [15,  12 , 8, 10], [[1, 2], [2, 4]])
# Out: 37
def computeTotal(root, weights, edges):
  def _loop(current):
    res = 0
    for edge in [edge for edge in edges if edge[0] == current]:
      res += _loop(edge[1]) + weights[edge[1] - 1]
    return res

  return _loop(root) + weights[root - 1]

# In : balancedForest([1, 2, 2, 1, 1], [[1, 2], [1, 3], [3, 5], [1, 4]])
# Out: 2
def balancedForest(c, edges):
  res = -1

  for x in edges:
    for y in [y for y in edges if y != x]:
      rest_of_edges = [z for z in edges if z != x and z != y]
      [r1, r2, r3] = [computeTotal(r, c, rest_of_edges) for r in [1, x[1], y[1]]]

      if r1 == r2:
        if res == -1 or (r1 - r3 < res and r1 - r3 > 0):
          res = r1 - r3

      elif r1 == r3:
        if res == -1 or (r1 - r2 < res and r1 - r2 > 0):
          res = r1 - r2

      elif r2 == r3:
        if res == -1 or (r2 - r1 < res and r2 - r1 > 0):
          res = r2 - r1

      else:
        pass

  return res
