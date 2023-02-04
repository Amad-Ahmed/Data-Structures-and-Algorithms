arr = [4, 2, 7, 8, 1, 3, 5, 6]
n = len(arr)
i = 0
while i < n-1:
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        temp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = temp
        j -= 1
    i = i+1

print(arr)
