# Objects are an encapsulation of variables and functions into a single entity. 
# Objects get their variables and functions from classes. 
# Classes are essentially a template to create your objects


class Myclass :
  variable = "random"

def function(self):
  print("This is a message inside the class.")


# to assign the above class to an object you would do the following:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

# Now the variable "myobjectx" holds an object of 
# the class "MyClass" that contains the variable and the function defined within the class called "MyClass".



# Accessing object variables

class MyClass :
   variable = "blah"

   def function(self):
      print("this is a message inside the class.")

myobjectx = MyClass()
print(myobjectx.variable)

# Accessing the variable ("blah") inside the class (MyClass) from the object (myobjectx)


# You can create multiple different objects that are of the same class(have the same variables and functions defined). However, 
# each object contains independent copies of the variables defined in the class. For instance, 
# if we were to define another object with the "MyClass" class and then change the string in the variable above:



class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)


# Accessing object functions

# to access a function inside of an object you use notation similar to accessing a variable

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()


# The above would print out the message, "This is a message inside the class."

# init()
# The __init__() function, is a special function that is called when the class is being initiated.

#  It's used for assigning values in a class.

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'