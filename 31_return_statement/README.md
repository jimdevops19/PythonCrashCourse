# Return Statement
## Return keyword used to give value back at the end of your functions, therefore, you could assign your function CALLS to variables and use their values later
```python 
#Each Function in Python has to give some value back when it completes the execution
#This is designed for assigning the call's of the function to a variable
#And make some uses with this variable in the future

#This case is going to return nothing, because we did not use return keyword
def square_my_number(num):
    print(num ** 2)

result = square_my_number(num=4)
print(result)

#So it is equvielant to this:
def square_my_number(num):
    print(num ** 2)
    return None

result = square_my_number(num=4)
print(result)

#But we could decide that we want to store within the result variable the value of 16
#To achieve this, we could write a code like that:
def square_my_number(num):
    return num ** 2

result = square_my_number(num=4)
print(result)

#Important to remember, that return is a signal for being the last line that will
#execute within a function, so something like this is pointless:

def square_my_number(num):
    return num ** 2
    print("One more line to print please") # UNREACHABLE CODE!

result = square_my_number(num=4)
print(result)


```

## Exercise:

### Insert those variables inside a formatted string, describe the print sentence the way you'd like
```python
favorite_language = "Python"
platform = "Youtube"
channel_name = "JSC"
```

### Answer:
```python
#We need to write some print lines starting with f letter before the single/double quotes
print(f"My favorite language now is {favorite_language}")
print(f"I learn about this language on {platform}")
print(f"The course I take now is on the channel of: {channel_name}")
```
