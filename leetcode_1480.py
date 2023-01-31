nums = [1,2,3,4]

for i in range(len(nums)):
    if i == 0:
        pass
    else:
        nums[i] = nums[i] + nums[i-1]
    
print(nums)