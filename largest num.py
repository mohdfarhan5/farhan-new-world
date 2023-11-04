def find_largest_number(arr):
    if not arr:
        return None  
    
    largest = arr[0]  
    
    for num in arr:
        if num > largest:
            largest = num  
            
    return largest

numbers = [20,25,10,45,22,50,40]
largest_number = find_largest_number(numbers)
print("The largest number is:", largest_number)
