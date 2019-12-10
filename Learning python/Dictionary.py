veg_pizza = {       #creating a dictionary
"size" : "medium",
"cost" : 5
}

hot_pizza = {}  #empty dictionary

print(veg_pizza["size"])    #get item from a dictionary
print(veg_pizza["cost"])

print("median veg pizza costs "+str(veg_pizza["cost"]))

print(veg_pizza)
veg_pizza["cheeseUsed"] = "mozarella" #adding to the dictionary
print(veg_pizza)

print("veg pizza price is increased, it was "+ str(veg_pizza["cost"])) #updating value in dictionary
veg_pizza["cost"] = 7
print("Veg pizza cost now is "+ str(veg_pizza["cost"]))

print(veg_pizza)
del veg_pizza["cheeseUsed"]
print(veg_pizza)

veg_pizza["cheeseUsed"] = "mozarella" #adding to the dictionary
veg_pizza["crustType"] = "deepPan"
print(veg_pizza)

for i in veg_pizza.keys(): #loop through key
    print(i)

for i in veg_pizza.values(): #loop through values
    print(i)

veg_pizza = {       #creating a dictionary
"size" : "medium",
"cost" : 5,
"base" : "deepPan"
}

meat_pizza = {
"size" : "medium",
"cost" : 6,
"base" : "thin"
}

hawai_pizza = {
"size" : "medium",
"cost" : 6,
"base" : "Italian"
}

pizzas = [veg_pizza,meat_pizza,hawai_pizza] #list of dict

for pizza in pizzas:
    print(pizza)

veg_pizza = {       #creating a dictionary with a list inside
"size" : "medium",
"cost" : 5,
"base" : "deepPan",
"toppings" : ["peppers","onions","tomato","jalapenos","mushrooms"]
}

print("Topping on the veg_pizza is ")
for topping in veg_pizza["toppings"]:
    print(topping)

restaurant = {
"location" : "England",
"restaurant_type" : "pizzaria",
"staff_Number" : 13,
"pizza" : {      #creating a dictionary within a dictionary
    "size" : "medium",
    "cost" : 5,
    "base" : "deepPan"
    }
}
