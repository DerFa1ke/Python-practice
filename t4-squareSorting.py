# Квадратичные соритровки массива А  

def insertSort (A) :
    """ Сортировка списка А вставками """
    for top in range(1, len(A)) :
        k = top 
        while k > 0 and A[k-1] > A[k] :
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1 

def choiseSort (A) :
    """ Сортировка списка А выбором """
    for pos in range(0, len(A)-1) :
        for k in range(pos+1, len(A)) :
            if A[k] < A[pos] : 
                A[k], A[pos] = A[pos], A[k]

def bubbleSort (A) :
    """ Сортировка списка А методом пузырька """
    for byPass in range(1, len(A)) :
        for k  in range(0, len(A)-byPass) :
            if A[k] > A[k+1] : 
                A[k], A[k+1] = A[k+1], A[k]


def testSort (sortDef) :
    """ Тестирующая функция """
    print("Тестируем: ", sortDef.__doc__)
    print("test #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_ok = [1, 2, 3, 4, 5]
    sortDef(A)
    print("Ok!" if A == A_ok else "Fail")

    print("test #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_ok = list(range(20))
    sortDef(A)
    print("Ok!" if A == A_ok else "Fail")

    print("test #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_ok = [1, 2, 2, 4, 4]
    sortDef(A)
    print("Ok!" if A == A_ok else "Fail")




if __name__ == "__main__" :
    testSort(insertSort)
    testSort(choiseSort)
    testSort(bubbleSort)
