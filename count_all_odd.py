print("Learning lists")

# Create a list of 10 random numbers

numlist = [10, 17, 28, 33, 36, 39, 42, 49, 53, 57, 60, 63, 71, 78, 88, 90, 100]

count=0
for x in numlist:
    r = x%2
    if r != 0:
      count +=1 

print (count) 

