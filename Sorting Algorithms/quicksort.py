

def quickSort(arr, low, high):
    if (low < high):
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    pass


def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    j = low
    while j <= high:
        if arr[j] < pivot:
            i += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        j += 1
    temp = arr[high]
    arr[high] = arr[i+1]
    arr[i+1] = temp
    return i+1


if __name__ == '__main__':
    arr = [4, 2, 7, 8, 1, 3, 5, 6]
    low = 0
    high = len(arr)-1
