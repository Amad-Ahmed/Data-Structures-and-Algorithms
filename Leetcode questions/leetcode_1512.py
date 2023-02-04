nums = [1,1,1,1]

i = 0
num_good_pairs = 0

while (i<len(nums)):
    j=0
    while(j<len(nums)):
        if (i == j):
            pass
        elif (nums[i] == nums[j] and i<j):
            num_good_pairs+=1
        j+=1 
    i+=1

print(num_good_pairs)