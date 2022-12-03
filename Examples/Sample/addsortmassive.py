# Слияние отсортированных массивов
def merge(A:list, B:list):
    C:list = [0]*(len(A)+ len(B))
    i=k=n=0
    while i<len(A) and k<len(B):
        if A[i]<=B[k]:
            C[n]=A[i]
            i+=1
            n+=1
        else:
            C[n]=B[k]
            k+=1
            n+=1
    while i<len(A):
        C[n]=A[i]
        i+=1
        n+=1
    while k<len(B):
        C[n]=B[k]
        k+=1
        n+=1
    return C


#merge((1,2,5),(3,5,6))

# рекуреннтная сортировка слиянием
def merge_sort(A:list):
    C = [0]*len(A)
    if len(A)<=1:
        return
    middle=len(A)//2
    L=[A[i] for i in range (0,middle)]
    R=[A[i] for i in range (middle,len(A))]
    merge_sort(L)
    print(L)
    merge_sort(R)
    print(R)
    C=merge(L,R)
    print(C)
    for i in range(len(A)):
        A[i]=C[i]
    print(A)

merge_sort([7,3,1,2,6,4])

    
