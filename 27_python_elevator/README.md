# Python Elevator Exercise
## Write a program that will simulate the way that an elevator works. More instuctions could be found in the file:
```python 
#We should receive an input always
#User may write a number or out
#If he writes number, we should write him you are on {number} floor
#If he writes out, we should stop execution

#Improvement:
#The building has 20 floors
while True:
    answer = input("Which floor you want me to take you?")
    if answer == "out":
        print("Exiting...")
        break
    else:
        answer_floor = int(answer)
        if answer_floor >= 0 and answer_floor <= 20:
            print(f"You are on floor number {answer}")
        else:
            print(f"I can not take you to {answer_floor}")

#Great addition you can apply, the program should write "You are already on this floor", if you give the same floor number like the latest input
```