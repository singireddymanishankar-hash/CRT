''' 1 .square star pattern'''
  
'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''
    
'''2. right angle triangle star pattern'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''3. reverse right angle triangle star pattern'''
n = int(input())
for i in range(n, 0, -1):
    print("*" * i)
'''4. pyramid star pattern'''   
n = int(input())
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))