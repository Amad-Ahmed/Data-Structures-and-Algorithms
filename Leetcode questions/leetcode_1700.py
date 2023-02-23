queue = []
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
check_complete_rotation = len(students)

while check_complete_rotation > 0:
    print("Print in loop :: ")
    print(students)
    print(sandwiches)
    if students[0] == sandwiches[0]:
        students.pop(0)
        sandwiches.pop(0)
        check_complete_rotation = len(students)
        print("Print in if :: ")
        print(students)
        print(sandwiches)
    else:
        temp = students.pop(0)
        students.append(temp)
        check_complete_rotation -= 1
        print("Print in else :: ")
        print(students)
        print(sandwiches)
