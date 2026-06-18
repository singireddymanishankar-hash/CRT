import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from shared_utils.pattern_utils import (
    diamond_pattern,
    number_pyramid_pattern,
    hollow_pyramid_pattern,
    print_pattern,
)

#li=[1,2,3,4,5]
#output:{1,4,9,16,25}

'''li=[1,2,3,4,5]
s=[]
for i in li:
    s.append(i**2)
print(s)

ans=[i**2 for i in li]
print(ans)'''

'''pyramid star pattern (diamond)'''
'''n=int(input())
print_pattern(diamond_pattern(n))'''

'''Number pyramid pattern'''
n = int(input())
print_pattern(number_pyramid_pattern(n))

'''Hollow pyramid'''
n = int(input())
print_pattern(hollow_pyramid_pattern(n))
