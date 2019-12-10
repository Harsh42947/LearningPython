objs = ["bat","cat","mat","pat","hat","flower"]

for obj in objs:
    if obj == "cat":
        print ("Cat found")
    else:
        print("Cat not found here")


for obj in objs:
    if obj == "cat" or obj == "bat": #can add logic conditions to if
        print ("Animal found")
    else:
        print("Animal not found here")

if "flower" in objs:
    print("Flower is in the list")

if "Rambo" in objs:
    print("Rambo is in the list")

if "Rambo" not in objs:
    print("Rambo is not in the list")

pizzatop = []

if pizzatop:
    for i in pizzatop:
        print("you want " + pizzatop[i] +" on your pizza")
else:
    print("Your pizza is empty")

pizzatop = ["peppers","mushrooms","tomato","sweetcorn","jalapenos"]

if pizzatop:
    for i in pizzatop:
        print("you want " + i +" on your pizza")
else:
    print("Your pizza is empty")
