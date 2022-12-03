def shift_array(A:list,N:int):
    """циклический сдвиг массива влево
    """
    tmp=A[0]
    for k in range(N-1):
        A[k]=A[k+1]
    A[N-1]=tmp
def test_shift_array():
    A=[1,2,3,4,5]
    print(A)
    shift_array(A,5)
    print(A)
    if A==[2,3,4,5,1]:
        print("#test1-ok")
    else:
        print("#test1-false")   

test_shift_array()

def shift_array(A:list,N:int):
    """циклический сдвиг массива вправо
    """
    tmp=A[N-1]
    for k in range(N-2,-1,-1):
        A[k+1]=A[k]
    A[0]=tmp
def test_shift_array():
    A=[1,2,3,4,5]
    print(A)
    shift_array(A,5)
    print(A)
    if A==[5,1,2,3,4]:
        print("#test1-ok")
    else:
        print("#test1-false")   

test_shift_array()


          

