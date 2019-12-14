"""Files and Exceptions Learning"""

#pi_digits.txt : 3.1415

try:
    with open("pi_digits.txt") as file_object: #open the file
        contents = file_object.read()  #store contents as a var
        print(contents)

    birthday = input("Enter birthday in format DDMMYYYY: ")
    if birthday in contents:            # check if a string is in another string
        print("Birthday is in pi")
    else:
        print("Birthday not in pie")

    filename = "programming.txt"
    #"w" for writing to a new file
    #"a" for writing for a existing file
    with open(filename,"w") as file_object:   #writing to a file
        file_object.write("I love Programming\n") #\n gives a new line
        file_object.write("Or do I ...")
except FileNotFoundError:
    print("Could not find the file")
    #pass : can be used to silently brush of the error without doing nothing

title = "Alice in Wonderland" #split up string by spaces and put in list
print(title.split() )
