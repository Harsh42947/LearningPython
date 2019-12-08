obj = []
obj = ["bat","cat","pat"]
print(obj)

print(obj[0])

print(obj[-1]) #get me the last elem in a list

obj[0] = "tab" # change the element of the list
print(obj[0])

obj.append("banana") #add to the list
print(obj)

obj.insert(2,"flowers") #insert at specific index)
print(obj)

del obj[0] #delete element at index, pop function can also be sued to pop last element and return it
print(obj)

popedObj = obj.pop(2)
print(obj)
print(popedObj)

obj.remove("cat") #remove specific element
print(obj)

nums = [1,5,2,7,45,2,5,9]
print(nums)

print(sorted(nums)) #temporaraly sorts the list, then unsorts it
print(nums)

nums.sort() # sorts the list forever
print(nums)

nums.reverse() #reverse a list
print(nums)
print(len(nums)) #get the length of a list
