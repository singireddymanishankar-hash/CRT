import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from shared_utils.digit_utils import (
    count_digits,
    sum_of_digits,
    extract_even_digits,
    reverse_number,
    is_palindrome_number,
)

'''1. Count digits'''
'''N=int(input())
print(count_digits(N))'''

'''2. Sum of digits'''
'''n=int(input())
print(sum_of_digits(n))'''

'''3. Print even digits (right-to-left)'''
'''n=int(input())
for d in reversed(extract_even_digits(n)):
    print(d, end=" ")'''

'''4. Print even digits (left-to-right using reverse)'''
'''n=int(input())
for d in extract_even_digits(n):
    print(d, end=" ")'''

'''5. Palindrome check'''
n = int(input())
temp = reverse_number(n)
print(temp == 0)
if temp == 0:
    print(True)
else:
    print(False)
print(True) if temp == 0 else print(False)
