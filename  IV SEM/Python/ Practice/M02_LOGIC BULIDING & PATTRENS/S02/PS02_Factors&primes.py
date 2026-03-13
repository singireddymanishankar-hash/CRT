'''
print all factors of a number

n=int(input())
for i in range(1,n//2+1):
    if n%i==0:
        print(i,end=" ")
print(n)       
        '''
'''count number of factors of a number '''
'''n=int(input())
count=0
for i in range(1,(n//2)+1):
    if n%i==0:
        count+=1
print(count+1)
'''
'''check if a number is prinm or not'''
'''n=int(input())
if n<=1:
    print("invalid")
else:
       
    for i in range(2,n):
        
        if n%i==0:
            
            print("not prime")
            break
    else:
        print("prime")'''
        
"print all the prime numbers in given range"
'''start =int(input())
end=int(input())
for n in range(start,end+1):
    counter=0
    for i in range(2,n//2+1):
        if n%i==0:
            counter+=1
    if counter==0:
        print(n,end=" ")
'''
'''def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
n=int(input())
print(factorial(n))'''

'''gcd'''''
