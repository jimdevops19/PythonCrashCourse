# Input built in function
## Input built-in function allows to receive input from the user while the programs runs. Program won't resume till you put your input
```python 
#We always want to assign the input built-in function to a variable
answer = input("How is the weather today")
print("The weather today is ", answer)

#You can force your inputs to receive specific types of variables:
current_year = 2021
answer = int(input("What is your age?")) # We could use any built-in conversion function here we'd like
print("Your year of birth is", current_year - answer)



```
## Exercise:

###  Write a program that will receive three inputs, grade_one, grade_two, grade_three. Try to write a program that will print the average of the received three grades.

### Answer:
```python
#We need to force each input to be integers (float would also work)
grade_one = int(input("What is the first grade?"))
grade_two = int(input("What is the second grade?"))
grade_three = int(input("What is the third grade?"))

avg = (grade_one + grade_two + grade_three) / 3
print("Average is:", avg)
```
