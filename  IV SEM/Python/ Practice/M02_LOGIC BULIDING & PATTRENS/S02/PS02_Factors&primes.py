import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..'))

from shared_utils.math_utils import get_factors, count_factors, is_prime, primes_in_range, factorial

'''print all factors of a number'''
'''n=int(input())
print(*get_factors(n))'''

'''count number of factors of a number'''
'''n=int(input())
print(count_factors(n))'''

'''check if a number is prime or not'''
'''n=int(input())
if n <= 1:
    print("invalid")
elif is_prime(n):
    print("prime")
else:
    print("not prime")'''

'''print all the prime numbers in given range'''
'''start = int(input())
end = int(input())
print(*primes_in_range(start, end))'''

'''factorial'''
'''n=int(input())
print(factorial(n))'''

'''gcd'''
