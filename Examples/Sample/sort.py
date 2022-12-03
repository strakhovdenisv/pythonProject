#Квадратичные сортировки
def insert_sort(A):
    """сортировка списка A вставками"""
    N=len(A)
    for top in range(1,N):
        k=top
        while k > 0 and A[k-1] > A[k]:
            A[k],A[k-1] = A[k-1],A[k]
            k-=1
            
def choise_sort(A):
    """сортировка списка A выбором"""
    N=len(A)
    for pos in range(0,N-1):
        for k in range(pos+1,N):
            if A[k] < A[pos]:
                A[k],A[pos]= A[pos],A[k]
                
def bubble_sort(A):
    """сортировка списка A методом пузырька"""
    N=len(A)
    for bypass in range(1,N):
        for k in range(0,N-bypass):
            if A[k] > A[k+1]:
                A[k],A[k+1]= A[k+1],A[k]

def test_sort(sort_algorithm):
    print("Тестируем. ",sort_algorithm .__doc__)
    print("testcase #1:", end="")
    A=[4,2,5,1,3]
    A_sorted=[1,2,3,4,5]
    sort_algorithm(A)
    print("Ok" if A==A_sorted else "Fail")

    print("testcase #2:", end="")
    A = list(range(10,20)) + list(range(0,10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3:", end="")
    A = [4,2,4,2,1]
    A_sorted = [1,2,2,4,4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")


test_sort(insert_sort)
test_sort(choise_sort)
test_sort(bubble_sort)

#Сортировка подсчетом
A=[1,5,7,8,4,7,0,3,7,1,2,5,7,8,9]
N=len(A);F=[0]*10
for i in range(N): #частотный анализ
    x=A[i]
    F[x]+=1
print(F)

B=[]
for digit in range(10):
    x=F[digit]
    while x>0:
        B.append(digit)
        x-=1
  
print(B)




