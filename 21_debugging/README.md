# Debugging
## Debugging is the process of locating and eliminating problems within our code execution.
```python 
#Each IDE will have its own utilities to run programs in debugging mode.
#Debugging could be extremely useful because it gives us the ability to execute code line by line.
#And it gives us full control for the execution which could be helpful for complex programs.
friends = ["Allen", "Ben", "John", "Michael", "Jim"]
best_friend = "Allen"
#Write a program that will check if our best_friend is in
#the friends list. If so, throw a special message.

#Solution 2:
for friend in friends:
    if friend == best_friend:
        print(f"{best_friend} is inside the list!")


#How to debug with Pycharm?
#You can use the shortcut of SHIFT + F9 to debug.
#IMPORTANT: You should mark some line of code as a break point to initialize debug successfully.
```