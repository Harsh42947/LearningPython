#variables
hello = "Hello world"
print(hello)
hello = "Hello world 2"
print(hello)

#Strings
name = "john doe"
print(name.title()) #make first ltter of first and last name capital
name = "john doe"
print(name.upper()) #make string all capital
print(name.lower()) #make string all lower case

first = "john"
last = "doe"
full_name = first + " " + last
print(full_name)

print("Hello " + name.title() + " !")
msg = "Hello " + name.title() + " !"
print(msg)

print(" J \n U \n S \n T")

unstrip = "     JUST"
print(unstrip)
strip = unstrip.lstrip() #lstrip is left strip and removes spaces from left side
print(strip)

age = 1000
print("i am "+ str(age) + " years old")
