accounts=[[1,2,3],[3,2,1]]
n =len(accounts)

richest=0
temp_richest=0
i = 0
while (i<len(accounts)):
    j=0
    while(j<len(accounts[i])):
        temp_richest=temp_richest+accounts[i][j]
        j+=1
    if(richest<=temp_richest):
        richest=temp_richest
    i+=1
    temp_richest=0
