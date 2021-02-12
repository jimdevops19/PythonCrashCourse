# Imports
## There are tons of external libraries in Python that you can use them by calling it's name using the built-in keyword import
```python 
import math

#For example, say that we want to perform some more complex
#Math operations, than we can go and import the math library
#And use its additional functionalities like that:
a = 8.2
b = math.floor(a)
c = math.ceil(a)
print(b)
print(c)

#Remember, there are some more ways that you can import
#Additional functionalities.
#You can refer to the specific function that you want to import
#FROM an external library

from math import ceil

#And then use it like:

d = 8.2
e = ceil(d)
print(e)

#But that approach is less common, since the
#Python will load the entire library anyway.
#We could think that importing specific function could improve
#the time run of our program, but this is not the case
```