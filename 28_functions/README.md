# Functions
## A function is a block of code which only runs when it is called.
```python 
#Lets write a special counting program
#You can CREATE a function by using the format:
#def <name>():
#<name> being the name that you'd like to give to your functions
def special_count():
    for i in range(1, 11, 1):
        print(f"Special count {i}")

#This is how you CALL to a function
special_count() #Call
special_count() #Call
special_count() #Call
```