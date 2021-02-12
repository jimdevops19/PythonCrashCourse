# Dictionary Methods
## There are a lot of dictionary will do different manipulations for you with the dictionaries that you work with
```python 
#   keys() - Will collect all the keys
#   values() - Will collect all the values
friend = {
    "name" : "Mike",
    "age" : 25,
    "is_male" : True,
    "weight" : 64.5
}
print(friend.keys())
print(friend.values())

#Those lines will return you a type of variable
#That it's name is dict_keys

#To make it more friendly, we can convert it to a list:

print(list(friend.keys()))
print(list(friend.values()))


#There are more useful methods that you can take a look in python official documentation


```
## Exercise:

### In the given dictionary that describes names - age, Write the following programs:
 - Part 1: Write a program that will check if your best friend (Mike) is inside this dictionary, if so give the value (age) that attached to this key
 - Part 2: Search for a dictionary method that will DELETE a key&value pair from a dictionary.And then, delete the first key&value pair from this dictionary

### HINT: You can use in operator, to check if element is inside a list, for example:
```python
check = "Jim" in ["Jim", "John"]
print(check) # Will give True!
#Given Dictionary:
friends = {
    "Jack" : 22,
    "Mike" : 31,
    "Paul" : 18,
    "Mark" : 33
}
```

### Answer:
```python
#First Part:
keys = list(friends.keys())
best_friend = "Mike"
if best_friend in keys:
    best_friend_age = friends["Mike"]
    print(f"{best_friend} is {best_friend_age} years old!")

#Second Part:
keys = list(friends.keys())
first_key = keys[0]
friends.pop(first_key)
#Verify if this one worked:
print(friends)
```

