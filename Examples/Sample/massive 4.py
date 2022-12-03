A=[x**2 for x in range(10)]
#это эквивалент
A=[]
for x in range(10):
    A.append(x**2)
    
A=[1,2,-3,4,5,7,12,-9,6]    
B=[x**2 for x in A if x%2==0]
print(B)
#это эквивалент
B=[]
for x in A:
    if x%2==0:
            B.append(x**2)
print(B)

T=1,2,3,4,5
a,b,c,*rest = T
print(rest)
print(*rest,sep=":",end="!\n")

            
