# Break Statement
## Break keywords are available to use within loops, to immediately getting out of a for loop execution
```python 
#We should use break keyword when we want to get out of the associated for loop,
#Usually we will do it to check some condition in each iteration, and once we hit true, then we will use break.
#This is useful to efficient our program, and to prevent from unnecessary executions

#Example:
friends = ["Allen", "Ben", "John", "Michael", "Jim"]
best_friend = "Allen"

#Write a program that will check if our best_friend is in
#the friends list. If so, throw a special message.

#Solution:
for friend in friends:
    if friend == best_friend:
        print(f"{best_friend} is inside the list!")
        break
    else:
        print(f"This is {friend}")

print("I am just a random line after the for loop")
```