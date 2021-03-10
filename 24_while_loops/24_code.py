#While Loops

#We can use While loops to run some bunch of code till a condition changes after a while


#Example:
budget = 1000
sandwich_price = 5

while budget > 0:
    #Budget is currently greater than 0, it will remain like that, until we actually do something to prevent this from running forever within the while loop.
    #Usually we use while loops, it is important to have atleast one line of code that will affect the provided condition after the while keyword, otherwise, we will end up with having a endless loop
    print("You bought a sandwich!")

    budget -= sandwich_price #As you can notice here, we have a line that AFFECTS the budget's value.

print(budget)