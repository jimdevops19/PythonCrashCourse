# String Methods
## String has its unique methods to display them in different ways
```python 
#Here are some example you can try to execute:

#.title() - Will capitalize each word on the string
#.capitalize() - Will capitalize the first letter ONLY
#.upper() - Will turn all letters in uppercase
#.lower() - Will turn all lower in uppercase
name = "John doe"
print(f"Title: {name.title()}")
print(f"Capitalize: {name.capitalize()}")
print(f"Upper: {name.upper()}")
print(f"Lower: {name.lower()}")
```

## Exercise:

###  Is there a way to see how many characters we have inside a string ? Try to search for a way to do so.
```python
course_name = "JimShapedCoding" # We should find a python built-in function that will automatically count the characters, and give us back 15
```

### Answer:
```python
#len - A built-in function that will allow us to count the number of characters in a string. We will use the len built-in function as well in more complex variable types that we will learn in the future
course_name_length = len(course_name)
print(course_name_length) #Will return 15
```