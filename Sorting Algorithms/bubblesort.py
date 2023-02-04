arr = [4, 2, 7, 8, 1, 3, 5, 6]
n = len(arr)
updated_len = n
swap = True
i = 0

while i < n:
    print(i)
    j = 0
    swap = False
    while j < updated_len-1:
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            swap = True
        j += 1
    updated_len -= 1
    if swap == False:
        break
    i += 1

print(arr)
