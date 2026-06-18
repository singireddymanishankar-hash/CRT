import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from shared_utils.series_utils import fibonacci_recursive

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_recursive(n))
