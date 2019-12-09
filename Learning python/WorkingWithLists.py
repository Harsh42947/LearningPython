obj = ["cat","hat","bat","mat","pat","fridge","potato"]
# looping through a list
for objs in obj:
    print(objs)

for vals in range (1,6): #gives all numbers 1-5 NOT 1-6
    print(vals)

nums = list(range(1,10)) #list function turns range into a list
print(nums)

odd_nums = list(range(1,10,2)) #odd numbers, starts at 1 and adds 2 each time
print(odd_nums)

square_nums = []            # print square numbers
for val in range(1,11):
    square = val ** 2
    square_nums.append(square)

print(square_nums)

print(min(square_nums))     #get min and max of a list
print(max(square_nums))

square_nums = [values ** 2 for values in range(1,11)]
print(square_nums)

rand = [1,5,3,6,4,5,8,4,67]
print(rand)
print(rand[0:4]) #split the list and get elem 0-3 NOT 0-4
print(rand[4:])  #print 4 onwards
print(rand[-2:]) # print last 2

rand2 = rand[:] #makes a copy of a list
print(rand2)

tup = (10,100) #tuple, cant change its value once its assigned
print(tup[0])
print(tup[1])

for dimenttions in tup: #loop throught the elems in the tuple
    print(dimenttions)
