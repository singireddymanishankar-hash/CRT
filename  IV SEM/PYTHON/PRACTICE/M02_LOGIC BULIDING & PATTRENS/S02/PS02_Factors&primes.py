'''
print all factors of a number

n=int(input())
for i in range(1,n//2+1):
    if n%i==0:
        print(i,end=" ")
print(n)       
        '''
'''count number of factors of a number '''
        
n=int(input())
count=0
for i in range(1,(n//2)+1):
    if n%i==0:
        count+=1
print(count+1)