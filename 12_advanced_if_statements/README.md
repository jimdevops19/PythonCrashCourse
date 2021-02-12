# Advanced If Statements
## Expressions could be merged with some special keywords like **and**, **or** and it could add more complexity to our If statements
```python 
#Those keywords are also known as Logical Operators:

#and  - True if both statements are true
#or	  - True if one of the statements is true
#not  - Reverses the result of the statement

is_snowing = True  #Change this to test the results
is_raining = False #Change this to test the results

is_hot = not is_snowing
is_cold = is_snowing or is_raining
both_snowing_and_raining = is_snowing and is_raining

print(f"Is Cold: {is_cold}")
print(f"Is Hot: {is_hot}")
print(f"Both Snowing And Raining: {both_snowing_and_raining}")



```
## Exercise:

### Write a Program that simulates registration to a website. You need to receive those 3 inputs:
 - Username
 - Password
 - Confirm Password

### Your Registration System must meet those requirements:
 - Username's length includes atleast 6 or more characters
 - Password matches the Confirm Password

### Suggestion: Write if statement that will include AND logical operator and show a nice print message if the given info is good (meets the requirements) or not good

### Answer:
```python
#We need to start with three inputs
username = input("What is your username?")
password = input("What is your password?")
confirm_password = input("Please confirm Password?")

first_requirement = len(username) >= 6 #If you remember, len is the built-in function to give the amount of characters in a given string
second_requirement = password == confirm_password

if first_requirement and second_requirement:
    print("Your account has been created!")
else:
    print("Something went wrong with the registration")

#There are more requirements that you can apply on this program, obviously, it wouldn't be nice to register users if they will provide in passwords with two characters.
#There are always tons of ways to improve any program!
```

