import math
import os
import random
import re
import sys

def morganAndString2(a, b):
    result=''
    i=0
    j=0

    while i < len(a) or j < len(b):
        
        if i < len(a) and j < len(b):
            _a = a[i]
            _b = b[j]

            if _a <_b:
                result+=_a
                i+=1
                continue
            elif _b < _a:
                result+=_b
                j+=1
                continue
            else:
                v=_a
                next_a=i+1
                next_b=j+1
                
                if next_a < len(a) and next_b < len(b):
                    if a[next_a] == b[next_b] and v < a[next_a] and v < b[next_b]:
                        result+=v
                        result+=v
                        i+=1
                        j+=1
                        continue

                    elif a[next_a] < b[next_b]:
                        result+=v
                        i+=1
                        continue
                    
                    elif b[next_b] < a[next_a]:
                        result+=v
                        j+=1
                        continue

                    else:
                        result+=v
                        i+=1
                        continue
            
                else:
                    if next_a >= len(a) and next_b < len(b) and b[next_b] < v:
                        result+=v
                        j+=1
                        continue
                    elif next_b >= len(b) and next_a < len(a) and a[next_a] < v:
                        result+=v
                        i+=1
                        continue
                    else:
                        result+=v
                        i+=1
                        continue
                            
        elif i < len(a) and j == len(b):
            result+=''.join(a[i:])
            break

        elif i == len(a) and j < len(b):
            result+=''.join(b[j:])
            break

        else:
            pass


    return result
