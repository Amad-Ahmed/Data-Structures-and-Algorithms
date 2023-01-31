
number = 12345
# First check number of digits in number
length=1
while((number%(10**length)) != number):
    length+=1

print(length)

# Now iterate accordingly to calculate sum
sum = 0
while(length>=0):
    sum = sum + int((number % (10**length))/10 ** (length-1))
    length-=1
print(sum)
