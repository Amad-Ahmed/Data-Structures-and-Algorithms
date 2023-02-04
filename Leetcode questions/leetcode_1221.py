s = "RLRRLLRLRL"
r_count = 0
l_count = 0
count = 0
i = 0

for i in range(len(s)):
    if(s[i] == "R"):
        r_count+=1
    if(s[i] == "L"):
        l_count+=1
    if(r_count == l_count):
        count+=1

print(count)