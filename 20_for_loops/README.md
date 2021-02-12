# For Loops
## For loops allows to execute action circularly, depending on the variable type that you apply the for loop on
```python 
friends = ["Allen", "Ben", "John", "Michael"]
#With this approach, we print the information we want
#But this will require from us to edit our code if we will
#decide one day to add some more friends:

#print(f"{friends[0]} is my friend")
#print(f"{friends[1]} is my friend")
#print(f"{friends[2]} is my friend")
#print(f"{friends[3]} is my friend")

#For loops:
#A for loop is used for iterating over a sequence (in this case we have a list.)
#For loop template:

# for ____ in ______
#   new_var   iterable variable type   
for my_friend in friends:
    print(f"{my_friend} is my friend")


#An Exercise that we have done in the tutorial:

friends = ["Allen", "Ben", "John", "Michael", "Jim"]
best_friend = "Allen"
#Write a program that will check if our best_friend is in
#the friends list. If so, throw a special message.

#Solution 1:
if best_friend in friends:
    print(f"{best_friend} is in the list of friends!")

#Solution 2:
for friend in friends:
    if friend == best_friend:
        print(f"{best_friend} is inside the list!")
```