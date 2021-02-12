#Value Decrement and Increment

#Value decrement and increment is the process of reassigning a value to an existing variable name.


#Example:
age = 24
#Besides using:
age = age + 1
#We could use:
age += 1
#Or besides using
age = age - 1
#We could use
age -= 1

#An example we showed in the tutorial:
budget = 100
sandwich_price = 5

#Let's buy 20 sandwiches program!
#budget should decrease by 5 each time you print
#you bought a sandwich
for s in range(20):
    print("You bought a sandwich!")
    budget -= sandwich_price #Python Decrement
print(budget)

#You can also use increment like that:
#budget += 10 # Python Increment