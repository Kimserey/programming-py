import math
import os
import random
import re
import sys

'ABX' 'A'

def ms2(a, b):
    result=''
    i=0
    j=0

    while i < len(a) or j < len(b):
        if i < len(a) and j >= len(b):
            result+=''.join(a[i:])
            break

        elif i >= len(a) and j < len(b):
            result+=''.join(b[j:])
            break

        elif i < len(a) and j < len(b):
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
                # _a == _b
                v=_a
                next_a=i+1
                next_b=j+1

                # at the end of a and b and equal
                if next_a >= len(a) and next_b >= len(b):
                    result+=v
                    result+=v
                    i=len(a)
                    j=len(b)
                    continue
                
                while next_a <= len(a) or next_b <= len(b):
                    if next_a >= len(a) and next_b < len(b):
                        if v <= b[next_b]:
                            result+=a[i:]
                            result+=b[j:next_b]
                            i=len(a)
                            j=next_b
                        else:
                            result+=a[i:next_a]
                            result+=b[j:]
                            i=len(a)
                            j=len(b)
                        break

                    elif next_a < len(a) and next_b >= len(b):
                        if v <= a[next_a]:
                            result+=a[i:next_a]
                            result+=b[j:]
                            i=next_a
                            j=len(b)
                        else:
                            result+=a[i:]
                            result+=b[j:next_b]
                            i=len(a)
                            j=next_b
                            
                        break
                    
                    elif next_a == len(a) and next_b == len(b):
                        result+=a[i:next_a]
                        result+=b[j:next_b]
                        i=next_a
                        j=next_b
                        break
 
                    elif a[next_a] == b[next_b]:
                        if a[next_a] <= v:
                            next_a+=1
                            next_b+=1
                            continue
                        
                        elif v < a[next_a]:
                            result+=a[i:next_a]
                            result+=b[j:next_b]
                            i=next_a
                            j=next_b
                            break

                        else:
                            pass

                    elif a[next_a] < b[next_b]:
                        if v < a[next_a]:
                            result+=a[i:next_a]
                            result+=b[j:next_b]
                            i=next_a
                            j=next_b
                            break
                            
                        else:
                            result+=a[i:next_a]
                            i=next_a
                            break
                    
                    elif a[next_a] > b[next_b]:
                        if v < b[next_b]:
                            result+=a[i:next_a]
                            result+=b[j:next_b]
                            i=next_a
                            j=next_b
                            break
                            
                        else:
                            result+=b[j:next_b]
                            j=next_b
                            break

        else:
            pass


    return result
