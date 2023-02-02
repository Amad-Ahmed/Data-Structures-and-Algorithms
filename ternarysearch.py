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
l = 0
r = len(arr)-1

while l <= r:
    mid1 = int(l+(r-l)/3)
    mid2 = int(r - (r-l)/3)
    if target_element == arr[mid1] or target_element == arr[mid2]:
        print("Element found")
        break
    elif target_element < arr[mid1]:
        r = mid1
    elif target_element > arr[mid2]:
        l = mid2

    else:
        l = mid1
        r = mid2
if r == l:
    print("Element not found")
