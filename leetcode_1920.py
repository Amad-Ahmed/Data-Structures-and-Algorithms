nums=[5,0,1,2,3,4]
ans=[]
i = 0
for i in range(6):
    ans.append(nums[nums[i]])
    i=i+1
    print(ans)