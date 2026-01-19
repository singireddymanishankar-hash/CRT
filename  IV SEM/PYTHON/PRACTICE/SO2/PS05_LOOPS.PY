#counter=0
# while counter <5:
    # print("Helllo worlddd")
    # counter+=1
    
    
# start=int(input())
# stop=int(input())
# while start<= stop:
    # if start % 2==0:
        # print(start,end=" ")
    # start+=1
'''''  
start=int(input())
stop=int(input())
while start<=stop:
    if start%3==0 and start% 5==0:
        print("fizzbuzz")
    elif start%3==0:
        print("fizz")
    elif start %5==0:
        print("buzz")
    else:
        print(start)
    start+=1      
'''
''''
n=int(input())
for i in range(n,0,-1):
    print(i,end=" ")
    '''

li=[1,5,4,3,6,9,10]
for i in range(0,len(li),1):
    if li[i]% 2==0:
        print(li[i],end=" ")
    
    