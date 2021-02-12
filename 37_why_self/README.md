# Why self?
## Self is just a convention, the first parameter of an instance method could be named whatever you'd like to. But one param should be there and we will understand why.
```python 
#Let's say that we have this code right now:
class CreditCard:
    def __init__(self, number):
        self.number = number

    def hide():
        print("Hiding!")
        #self.number = f"**** **** **** {self.number[-4:]}"

c1 = CreditCard(number="1234567890123456")
c1.hide()

#As you can see, the hide() does not receive the self as a parameter.

#When we will execute that, we will receive:
#TypeError: hide() takes 0 positional arguments but 1 was given

#Positional Arguments stands for the amount of parameters,
#and what was given is an argument from the line c1.hide()

#So it means, that Python, in the background PASSES the instance itself as an argument to any method that it will execute
#So those two approaches are equivelant:
c1.hide()
CreditCard.hide(c1)

#And, to avoid passing the c1 always, we use the first approach

#Now that we understood why we have to ATLEAST provide one parameters, then, why self?
#Just a convention among all the python programmers, if you were to change this to any other word, this would work as well, but it is never necessary

```