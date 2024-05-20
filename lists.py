print("Learning lists")

# Create a list of 10 random numbers

numlist = [10, 28, 36, 42, 53, 60, 78, 88, 90, 100]
print(numlist[5])
print(numlist.index(42))
print("-----------------")

# to loop
# for variable in list_name:
#      do something with variable
x = 0
count = 0
for x in numlist:
    if x > 20:
        print(x)
    count += 1
print("---------------------")   
print(count)






