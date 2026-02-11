'''N=int(input())
count=0
while N>0:
    count+=1
    N=N//10
print(count)#'''


'''n=int(input())
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print(sum)'''
 
'''n=int(input())
while n>0:
    
    digit=n%10
    if digit%2==0:
        print(digit,end=" ")
    n=n//10'''
    
'''def reverse(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    return rev
n=reverse(int(input()))
while n>0:
    digit=n%10
    if digit%2==0:
        print(digit,end=" ")
    n=n//10'''
    
    n=int(input())
    temp=reverse(n)
    print(temp==0)
    if temp==0:
        
        print(True)
    else:
        
        print(False)    
    print(True)if temp==0 else print(False)        
    