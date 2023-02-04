nums = [1,2,3,4,4,3,2,1]
ans = []
half_len = int((len(nums))/2) # 3
i = 0
k = 0
j = half_len
while (i < half_len):
    ans.insert(k,nums[i])
    ans.insert(k+1,nums[j])
    k+=2
    j+=1
    i+=1
print(ans)