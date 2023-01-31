s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
list1=list(s)
string_copy = s

i = 0 
for i in range(len(indices)):
    list1[indices[i]] = s[i]

string_copy = ''.join(list1)
print(string_copy)