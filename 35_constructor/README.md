# Constructor / __init__()
## Constructor will help us to pass in unique info per instance when we initialize an instance
```python 
#In this Example, we create the instances of class successfully, with all the wanted attributes, but we have some problems:
#First, we need to provide hardcodedly the info about number, limit, company each time. It could have been nicer if we would have the class as a class that expects for these pieces of info, before we initialize an instance of it.
#Because, we could still create more instances, without really creating credit card numbers, which makes zero sense.

class CreditCard:
    pass

c1 = CreditCard()
c1.number = "1234567890123456"
c1.limit = 5000
c1.company = "JimCompany"

c2 = CreditCard()
c2.number = "9876543210123456"
c2.limit = 2500
c2.company = "JohnCompany"

c3 = CreditCard()
c3.number = "1234567899876543"
c3.limit = 1000
c3.company = "MikeCompany"


#We could launch an init method that will help us to handle what happens when an instance of a class is created, because it automatically gets called:
class CreditCard:
    def __init__(self):
        print("I am created!")

c1 = CreditCard() # Will print 'I am created'


#The self keyword is a parameter convention name that will refer always to the instance of the class

#Now we might want to initialize some attributes that are going to be unique per instance. This could be done like this:

class CreditCard:
    def __init__(self, number):
        self.number = number

c1 = CreditCard(number="1234567890123456")
c2 = CreditCard(number="1234567894567891")
c3 = CreditCard(number="9876543210123456")
c4 = CreditCard(number="1234567895645621")


print(c1.number)
print(c2.number)
print(c3.number)
print(c4.number)

#Exercise we have done in the tutorial
#Add 2 more instance attributes that must be launched when the instances are created

#Solution:

class CreditCard:
    def __init__(self, number, limit, company):
        self.number = number
        self.limit = limit
        self.company = company

# Add 2 more instance attributes to this class: limit, company

c1 = CreditCard(number="1234567890123456", limit=1000, company="JimCompany")
c2 = CreditCard(number="1234567894567891", limit=2500, company="JohnCompany")

print(c1.limit)
print(c1.company)
print(c2.limit)
print(c2.company)

#We could use mandatory, non mandatory parameters like we learned in function.
#NOTE: NON Mandatory parameters must come as the last parameter when you put in your parameters

#This is not valid:
def __init__(self, number, limit=2000, company):
    pass #throwing pass just for example

#This is valid:
def __init__(self, number, company, limit=2000):
    pass #throwing pass just for example
```