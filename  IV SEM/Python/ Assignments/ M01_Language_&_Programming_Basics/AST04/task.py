import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from shared_utils.string_utils import reverse_string


def Reverse_String(s: str) -> str:
    return reverse_string(s)


if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))
