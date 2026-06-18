import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from shared_utils.series_utils import (
    arithmetic_series,
    geometric_series,
    fibonacci_iterative,
    factorial_series,
)

'''arithmetic series'''
'''n=int(input())
a=int(input())
print(*arithmetic_series(n, a, 10))'''

'''geometric series'''
'''n=int(input())
r=int(input())
print(*geometric_series(n, r, 10))'''

'''fibonacci series'''
'''n=int(input())
print(*fibonacci_iterative(n))'''

'''factorial series'''
n = int(input())
print(*factorial_series(n))
