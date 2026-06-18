import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from shared_utils.pattern_utils import (
    square_pattern,
    right_triangle_pattern,
    inverted_right_triangle_pattern,
    pyramid_pattern,
    print_pattern,
)

'''1. square star pattern'''
'''n=int(input())
print_pattern(square_pattern(n))'''

'''2. right angle triangle star pattern'''
n = int(input())
print_pattern(right_triangle_pattern(n))

'''3. reverse right angle triangle star pattern'''
n = int(input())
print_pattern(inverted_right_triangle_pattern(n))

'''4. pyramid star pattern'''
n = int(input())
print_pattern(pyramid_pattern(n))
