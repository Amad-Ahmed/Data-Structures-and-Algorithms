

num = ord('a')

sentence = "thequickbrownfoxjumpsoverthelazydog"
check = False
x = ord(sentence[15])
print(x)
for i in range(len(sentence)):
    check = False
    
    for j in range(len(sentence)):
        if (num == ord(sentence[j])):
            check = True
        
    if(check == False):
        print("FAlse")
    else:
        num = num + 1
print("True")
