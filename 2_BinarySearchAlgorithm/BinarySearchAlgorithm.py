def binary_search(arr, target):
    # Defining left and right pointers
    left, right = 0, len(arr)-1
    
    while left <= right:
        # Finding the middle index
        mid_i = ( left + right ) // 2
        
        # Checking if the target is at the middle
        if target == arr[mid_i]:
            return mid_i
        
        # Checking if target is smaller than mid value
        elif target < arr[mid_i]:
            right = mid_i - 1       # ignoring the right half
            
        # Else (if target value is larger than mid value)
        else:
            left = mid_i + 1    # ignoring the right half
    
    return -1       # returning -1 if the target is not found in the list


arr = [23, 45, 34, 67, 31, 78, 90]
target = 78

index = binary_search(arr, target)

if index != -1:
    print(f"Target {target} is at the index {index}")
else:
    print(f"Target {target} not found.")
