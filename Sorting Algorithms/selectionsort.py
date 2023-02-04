arr = [4, 2, 7, 8, 1, 3, 5, 6]
n = len(arr)
i = 0
min = 1000
j = 0
index = 0
while i < n:
    j = i
    while j < n:
        if (arr[j] < min):
            min = arr[j]
            index = j
        j += 1
    temp = arr[i]
    arr[i] = min
    arr[index] = temp
    min = 1000
    i += 1
print(arr)
