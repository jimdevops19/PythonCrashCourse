#Classes

#Classes are definitions/blueprints to a realistic information that you want to maintain through program execution, basically the way to create your customized variable type


#Those are the built-in variable types that we learned
#until this point

#Strings
#Integers
#Floating Numbers
#Booleans
#Lists
#Dictionaries
#Tuples

#What is so special with those variable types, it is the fact
#that they have their own methods.

#Now if one day we want to create our own variable type,
#this is something that we can do
#And the following are good candidates for variables types,
#that you might want to create:

#CreditCard - hide() show() pay()
#Person - talk() run() play()
#Car - drive() stop() park()

#We can create our own variable types, using Classes

class CreditCard:
    pass

name = "Jim" #Creating an instance of a string
my_card = CreditCard() #Creating an instance of a CreditCard

print(type(name)) #will print <class 'str'>
print(type(my_card)) #will print <class '__main__.CreditCard'

