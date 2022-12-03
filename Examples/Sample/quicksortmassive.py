# Сортировка Тони Хоара(QuickSort)
def hoar_sort(A):
    if len(A)<=1:
        return
    barrier=A[0]
    L=[]
    M=[]
    R=[]
    for x in A:
        if x < barrier:
            L.append(x)
            print(L)
        elif x == barrier:
            M.append(x)
            print(M)
        else:
            R.append(x)
            print(R)
    hoar_sort(L)
    hoar_sort(R)
    k=0
    for x in L+M+R:
        A[k]=x
        k+=1
    print(A)

hoar_sort((5,8,4,3,2,9))
