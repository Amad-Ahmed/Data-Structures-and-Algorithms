nums=[1,2,1]
ans=[]
x = len(nums)
n = x*2

for i in range(n):
    ans.insert(i,nums[i%x])
    print (ans)
print(ans)
