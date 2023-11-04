def ascending_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def descending_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


numbers = [12, 45, 3, 67, 1, 89, 34]

print("Original list:", numbers)


ascending_sort(numbers)
print("Ascending order:", numbers)


descending_sort(numbers)
print("Descending order:", numbers)