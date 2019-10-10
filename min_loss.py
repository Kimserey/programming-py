import math
import os
import random
import re
import sys

def minimumLoss(price):
    prices=sorted(enumerate(price), key= lambda p: p[1], reverse=True)
    
    res=-1
    for i in range(len(prices)):
        if i < len(prices) - 1 and prices[i][0] < prices[i+1][0]:
            
            diff=prices[i][1] - prices[i+1][1]
            
            if res==-1 or diff<res:
                res=diff
    
    return res