#li=[1,2,3,4,5]
#output:{1,,4,6,16,25}


'''li=[1,2,3,4,5]
s=[]
for i in li:
    s.append(i**2)
print(s)
 
ans=[i**2 for i in li]
print(ans)'''

---'''piramid star pattern'''
'''n=int(input())  
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i) '''

--'''Nummber pyramid pattern  '''
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()    


--'''Hollow pyramid'''
n=int(input())
