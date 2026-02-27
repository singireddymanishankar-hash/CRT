'''
arithemetic series
'''
'''n=int(input())
a=int(input())
for i in range(10):
    print(n + i * a,end=" ") 
    '''
'''geometric series'''
'''n=int(input())
r=int(input())
for i in range(10):
    print(n * (r**i),end=" ") 
    
    '''
'''fibonacci series'''

'''n=int(input())
a=0
b=1
for i in range(n): 
    print(a,end=" ")
    a,b=b,a+b'''
    
'''factorial series'''
n=int(input())
fact=1
for i in range(1,n+1):              
    fact=fact*i
    print(fact ,end=" ")