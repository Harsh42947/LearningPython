def greet_users():          #function that returns nothing
    print("Hello there.")

def greet_name(name):       #function that takes parameter
    print("Hello " + name)

def buy_a_potato(cost): #function that returns a value
    cost_of_potato = 23
    return cost - cost_of_potato

def full_name(fname,lname,mname = ""):
    if mname:
        return fname + " " + mname + " " + lname
    else:
        return fname + " " + lname

def build_person(fname,lname):  #returning a dictionary
    person = {
    "first_name" : fname,
    "second_name" : lname
    }
    return person

def print_list(list):           #function that takes in a list
    for item in list:
        print("Item in list is:",item)

def toppings(*tops):                #variable length argument like var-args
    print("Toppings in pizza are ",tops)

def profile(fname,lname,**addition):    # ** ised to create a dictionary of variale length inputs
    prof = {}
    prof["FirstName"] = fname
    prof["LastName"] = lname
    for key,value in addition.items():
        prof[key] = value
    return prof

def main():
    greet_users()
    name = input("Enter your name: ")
    greet_name(name)
    my_moneys = input("How much money i have: ")
    #print( buy_a_potato( int(my_moneys) ) )
    print("After buying a potato i have "+ str(buy_a_potato(int(my_moneys) ) ) )

    print(full_name("bob","ben","bosh"))
    print(full_name("biff","chip"))

    print( build_person("John","Doe") )
    print_list(["ping","pong"])

    toppings("peppers","tomato","mushrooms","sweetcorn")
    toppings("ham","pineapple")

    print(profile("John","Doe",location = "USA",favColour = "Yellow") )


main()
