import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from typing import List
from shared_utils.series_utils import collatz_sequence


def Collatz_Sequence(n: int) -> List:
    return collatz_sequence(n)


if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))
