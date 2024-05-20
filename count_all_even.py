print("Learning lists")

# Create a list of 10 random numbers

numlist = [10, 16, 28, 32, 36, 42, 45, 53, 57, 60, 66, 69, 78, 72, 88, 90, 98, 100]

count = 0
for x in numlist:
    r = x%2
    if r==0:
        count +=1

print(count)