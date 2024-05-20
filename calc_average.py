print("Learning lists")

# Create a list of 10 random numbers

numlist = [10, 16, 28, 32, 36, 42, 45, 53, 57, 60, 66, 69, 78, 72, 88, 90, 98, 100]

num_items = len(numlist)
total = 0
for x in numlist:
    total = x + total

avg = total/num_items
avg = round(avg,2)
print(avg)
            
