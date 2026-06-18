import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from shared_utils.pattern_utils import pascal_triangle_pattern, print_pattern

'''
1. Pascal triangle pattern
n=5
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
'''
n = int(input())
print_pattern(pascal_triangle_pattern(n))
