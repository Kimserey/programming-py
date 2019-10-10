import math
import os
import random
import re
import sys

def get_min(a, b, n):
    def is_end(x, y):
        return x == n-1 and y == n-1

    def is_in(x, y):
        return x >= 0 and x < n and y >= 0 and y < n

    def visit(visited, count, current):
        visited.add(current)

        (x, y)=current
       
        positions=[(x-a, y-b), 
            (x+a, y-b), 
            (x-a,y+b),
            (x+a, y+b), 
            (x-b, y-a),
            (x+b, y-a), 
            (x-b,y+a),
            (x+b, y+a)]

        filtered_positions=set()
 
        for p in positions:
            if is_end(p[0], p[1]):
                return count+1

            if is_in(p[0], p[1]) and p not in visited:
                filtered_positions.add(p)

        if len(filtered_positions) == 0:
            return -1

        res=-1
        for x in filtered_positions:
            r=visit(visited, count+1, x)

            if r > 0 and (res == -1 or r < res):
                res=r

        return res
    
    return visit({(0, 0)}, 0, (0, 0))
