jewels = "aA"
stones = "aAAbbbb"
m = len(jewels)
n = len(stones)
print(n)
j = 0
i = 0
count = 0
while (i< m):
    j = 0
    while(j<n):
        if(jewels[i] == stones[j]):
            count+=1
        j+=1
    i+=1
print(count)