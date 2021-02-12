#Methods

#Different variable types are going to have their unique methods


#This is the name of our person:
name = "John doe"

#Say that we want this person to have the name spelled as it supposed to be: John Doe
#We can launch this method:

print(name.title()) # Will print John Doe

#We might think that once you launch this method on the variable, it will override it for the rest of the program

#BUT:
#Lets write this program now:

name_two = "John doe"
name_two.title()
print(name_two) # This line will STILL show: John doe

#Reason:
#Not all the methods out there, will affect the value of the variable that you apply the method on.

#To really override the value itself, we can launch this:

name_three = 'John doe'
name_three = name_three.title()
print(name_three) # This line will print John Doe