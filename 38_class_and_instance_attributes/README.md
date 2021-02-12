# Class and Instance Attributes
## Not only we can assign attributes that are unique per instance, but we can create attributes that are considered as global among all the instances of a class
```python 
#Class attribute is an attribute that is going to be global for the class only, usually we create those to have shared information among all the class instances
#Example:

class CreditCard:
    limit_raise_amount = 1.5 # That is a class attribute
    def __init__(self, number, limit):
        self.number = number
        self.limit = limit

#The way that we could access those kind of attributes:

print(CreditCard.limit_raise_amount) # will print 1.5

#However, we also can access those, from the instances.

c1 = CreditCard("9876543210123456", 1000)
print(c1.limit_raise_amount) # Will print 1.5

#The biggest question is, why the instance itself has an access to a class attibute ?

#It is because instances in Python search for its attributes values hierarchically
#First, it will look if it found the attribute in the instance level
#If it did not found it there, then it will grab the value from the Class.

#And so, running code like this:
print(c1.limit_raise_amount) # will print 1.5

#Remember, we said that the instance will look for the attributes value in the instance itself first, so this means that if we were to run such a code:

c2 = CreditCard("1234569876543210", limit=2000)
c2.limit_raise_amount = 2

#Then, this will give 2:
print(c2.limit_raise_amount)
#Reason: The instance found the value of limit_raise amount in the instance level, so it does not have to go up to the class level to bring it's value.

#Exercise we have done in the tutorial:

#Write a method for raise_limit, that will go ahead and raise the limit of the credit card to: self.limit * CreditCard.limit_raise_amount

#Solution:
#Create a method and name it raise_limit that will really
#raise the limit from what it is, by 50%

class CreditCard:
    limit_raise_amount = 1.5
    def __init__(self, number, limit):
        self.number = number
        self.limit = limit

    def hide(self):
        self.number = f"**** **** **** {self.number[-4:]}"

    def raise_limit(self):
        self.limit = CreditCard.limit_raise_amount * self.limit
        print(f"Congratulations! New limit has been set to {self.limit} for card number: {self.number}")

c1 = CreditCard(number="1234567890123456", limit=1000)
c1.raise_limit()
c2 = CreditCard(number="9876542310123456", limit=1000)
c2.raise_limit()


```