import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from shared_utils.string_utils import is_palindrome_string

n = input()
if is_palindrome_string(n):
    print("palindrome")
else:
    print("not palindrome")
