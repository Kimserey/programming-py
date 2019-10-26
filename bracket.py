import math
import os
import random
import re
import sys

def isBalanced(s):
    stack=[]

    for s in s:
        if s == '[' or s == '(' or s =='{':
            stack.append(s)
        else:
            if len(stack) == 0:
                return 'NO'
            else:
                top = stack[len(stack) - 1]

                if top == '[' and s == ']':
                    stack.pop()
                elif top == '(' and s == ')':
                    stack.pop()
                elif top == '{' and s == '}':
                    stack.pop()
                else:
                    return 'NO'

    return 'YES' if len(stack) == 0 else 'NO'
