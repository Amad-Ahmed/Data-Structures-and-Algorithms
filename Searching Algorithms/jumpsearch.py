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

step = int(math.sqrt(len(arr)))
while (target_element < arr[step]):
    step += step
step -= step

# now performing Linear search
while step < len(arr):
    if (arr[i] == target_element):
        print("Element found at index :: " + str(i))
        break
    step += 1
if step == len(arr)-1:
    print("Element not found.")
