def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1;

arr = [23, 45, 34, 67, 31]
target = 67

position = linear_search(arr, target)

if position != -1:
    print(f"Target {target} is at the position {position}")
else:
    print(f"Target {target} not found.")