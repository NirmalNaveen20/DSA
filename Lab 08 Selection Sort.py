A = [] 
for v in range(8):
    A.append(int(input('Enter a number: ')))

print(A)

def SelectionSort(A):
    n = len(A)
    for j in range(0,n-1):
        smallest = j
        for i in range(j+1, n):
            if A[i] < A[smallest]:
                smallest = i
            A[j],A[smallest] = A[smallest], A[j]

SelectionSort(A)
print('Sorted Array : ', A)




