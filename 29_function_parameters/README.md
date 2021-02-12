# Function Parameters
## Parameters will help us to accept additional piece of information to execute them
```python 
#We can pass in the info when we call the functions
#The values that are passed in as info when you call a function, called arguments
def special_count(stop_count):
    for i in range(1, stop_count + 1, 1):
        print(f"Special count {i}")

special_count(5)  # Count from 1 to 5
special_count(10) # Count from 1 to 10
special_count(20) # Count from 1 to 20

#Arguments could be passed in by providing the parameter name as well:
special_count(stop_count=5)  # Count from 1 to 5
special_count(stop_count=10) # Count from 1 to 10
special_count(stop_count=20) # Count from 1 to 20

#Multiple Parameters
def special_count(stop_count, step):
    for i in range(1, stop_count + 1, step):
        print(f"Special count {i}")

special_count(stop_count=5, step=1) # Count from 1 to 5
special_count(stop_count=10, step=2) # Count from 1 to 10 step 2
special_count(stop_count=20, step=1) # Count from 1 to 20


#Mandatory / Non Mandatory Parameters
def special_count(stop_count, step=1):
    #stop_count - Mandatory Param, does not have default value
    #step - NON Mandatory Param, it has a default value
    for i in range(1, stop_count + 1, step):
        print(f"Special count {i}")

special_count(stop_count=5) # Count from 1 to 5
special_count(stop_count=10, step=2) # Count from 1 to 10 step 2
special_count(stop_count=20) # Count from 1 to 20
```