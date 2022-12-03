A=[0]*1000
top=0
x=int(input(1))
while x!=0:
    A[top]=x
    top+=1
    x=int(input(1))
for k in range(4,-1,-1):
    print(A[k])

def array_search(A:list, N:int, x:int):
    """существляет поиск числа х в массиве А
       от 0 до N-1 индекса включительно.
       Возвращает индекс элемента в массиве А.
       Или -1, если такого нет.
       Если в массиве несколько одинаковых элементов,
       равных х, то вернуть индекс первого по счету.
    """
    for k in range(N):
        if A[k]==x:
            return k

def test_array_search():
    A1=[1,2,3,4,5]
    m= array_search(A1,5,8)
    if m==-1:
        print ("#test1-ok")
    else:
        print ("#test1-fail")


    A2=[-1,-2,-3,-4,-5]
    m= array_search(A2,5,-3)
    if m==2:
        print ("#test2-ok")
    else:
        print ("#test2-fail")
    

    A3=[10,20,30,10,10]
    m= array_search(A3,5,10)
    if m==0:
        print ("#test3-ok")
    else:
        print ("#test3-fail")

test_array_search() 
