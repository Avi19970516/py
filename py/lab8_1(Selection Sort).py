A = []
for r in range(8):
    A.append(input("Enter number :"))
print A

def SelectionSort(A): #function definition
    n = len(A)
    for j in range (n-1): #or range(0,n-1) #to the 2nd last index
        smallest = j
        for i in range(j + 1,n):
            if A[i] < A[smallest]:
                smallest = i
        temp = A[j]
        A[j] = A[smallest]
        A[smallest] = temp

SelectionSort(A) #function call
print("Sorted Array : ")
print A
