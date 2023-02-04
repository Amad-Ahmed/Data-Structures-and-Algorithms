import math
arr = [2, 4, 5, 1, 12, 7, 6, 0]
target_element = int(input("Enter element to be searched :: "))
i = 0
j = 0
while i < len(arr):
    j = i+1
    while j < len(arr):
        if arr[i] > arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        j += 1
    i += 1
print(arr)

low = 0
high = len(arr)-1
mid = 0
while low <= high:
    mid = low+(((target_element-arr[low]) * (high-low))/(arr[high]-arr[low]))
    if target_element == arr[mid]:
        print("Element found")
        break
    elif target_element > arr[mid]:
        low = mid+1
    else:
        high = mid-1
