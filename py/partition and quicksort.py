a = []
for v in range (7):
    a.append(input("Enter number : "))
print (a)

def partition(a,p,r):
    x = a[r]
    i = (p-1)
    
    for j in range(p,r):
        if a[j] <= x:
            i = i + 1
            temp  = a[i]
            a[i] = a[j]
            a[j] = temp

    temp = a[i + 1]
    a[i + 1] = a[r]
    a[r] = temp
    return (i+1)

#n = len(a)
#partition(a,0,n-1)
#print(a)

def quicksort(a,p,r):
    if p < r:
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)

n = len(a)
quicksort(a,0,n-1)
print("Sorted array")
print(a)
