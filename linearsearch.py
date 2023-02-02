arr = [9, 10, 3, 12, 34, 56, 7, 3]

search_element = int(input("Enter Element to be searched in list :: "))
i = 0
while i < len(arr):
    if (arr[i] == search_element):
        print("Element found at index :: " + str(i))
        break
    i += 1
if i == len(arr)-1:
    print("Element not found.")
