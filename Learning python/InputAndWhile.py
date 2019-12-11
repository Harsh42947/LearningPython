name = input("Whats your name: ") #get the input but this will store as a string
print("Name given as input is "+name)

height = input("Whats your height: ")

if int(height) > 36:            #casing input to int
    print("can go on ride")
else:
    print("not tall enough to go on ride")

print(45 % 3) #modulo operator

current = 0

while current < 5:
    print("currently we are at " + str(current))
    current += 1            #python doesnt have the ++ like C and Java

quit = ""
while quit != "quit":                   #how to quit a loop
    quit = input("If you want to quit input 'quit':")

quit = ""
while True:                             #using break to quit a loop
    quit = input("If you want to quit input 'quit':")
    if quit == "quit":
        break

while True:
    skip = input("If you want to skip the text press 'q': ") #continue
    if skip == "q":
        continue
    print("adededaedwdwe")
    print("adededaedwdwe")
    print("adededaedwdwe")

#can also use the user input to interact with dictionaries
