word1=["ab","c"]
word2=["a","bc"]
string1=""
string2=""

for i in range(len(word1)):
    string1=string1+word1[i]
print(string1)
for i in range(len(word2)):
    string2=string2+word2[i]
print(string2)
if (string1 == string2):
    print("True") 
else:
    print("False")