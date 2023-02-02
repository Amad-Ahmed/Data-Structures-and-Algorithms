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
high = len(arr)
i = 1
while i < (high-low):
    if (arr[i] < target_element):
        i *= 2
    else:
        break
# Binary Search code
mid = 0
low = i/2
high = i

while low != high:
    mid = int((low+high)/2)
    if target_element == arr[mid]:
        print("Element Found")
        break
    elif target_element < arr[mid]:
        high = mid - 1
    elif target_element > arr[mid]:
        low = mid+1
if high == low:
    print("Element not found")
