""" A class that can be used to rep a dog"""
class Dog():    #use camelcaps for naming classes

    def __init__ (self,name,age):           #initialize a new obj, use this convention for name
        self.name = name
        self.age = age

    def bark(self):
        print(self.name.title() + " is now barking")

    def birthday(self):                     #update attributes of an object
        self.age += 1;
        print(self.name.title() , " had a birthday, age is now " , self.age )

class Wolf(Dog):            #subclass of Dog

    def __init__(self, name, age):
        super().__init__(name,age)   #dont need to include self when calling super

    def bark(self):
        print(self.name.title() + " is now barking VERY LOUD (because wolf)")


def main():
    my_dog = Dog("ben",3)               #creating a obj in Dog class
    print(my_dog.name , " is dog name") #accessing attributes of obj
    print(my_dog.age , " is the dogs age")
    my_dog.birthday()           #calling functions in class

    my_wolf = Wolf("Frank",5)
    print(my_wolf.name , " is wolf name") #accessing attributes of obj
    my_wolf.bark()                          #method overloading
    my_wolf.birthday()                      #method overriding



main()

#from classes import Dog  #will import the Dog class from this py file
# import classes #  THis will import the while py file and all classes
