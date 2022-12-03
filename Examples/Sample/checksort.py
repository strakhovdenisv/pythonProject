def check_sorted(A, ascending = True):
    """проверка отсортированности O(len(A))"""
    flag=True
    N=len(A)
    s=2*int(ascending)-1
    for i in range(0,N-1):
        if s*A[i]>s*A[i+1]:
            flag = False
            print("not")
            break
        print("yes")
    return flag


check_sorted((1,2,3,5,4))
