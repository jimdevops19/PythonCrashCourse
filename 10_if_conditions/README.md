# If Statements
## If statement will allow you to decide whether if to execute a bunch of code, depending on a result of an expression you define.
```python 
#This Program print's descriptive message about how John did in the last exam.
#If grade is greater than 70, then he passed the exam
grade_john = 80
if grade_john > 70:
    print("Congratulation! You passed the exam.")
else:
    print("You failed the exam!")
#Each if statement will usually have an else statement, to cover the cases that python did not enter the if statement.

#Some exercise we done throughout the tutorial:

# Write a multi-line message
student_name = "john michael"
is_snowing = True

# Program should print a well written email
# If John should go to school today or not
# Solution:

if is_snowing:
    print(f"""
Hi {student_name.title()}.
You should not come to school today.
Thanks, school management.
""")

else:
    print(f"""
Hi {student_name.title()}.
Today the weather is fine, so please come to school.
Thanks, school management.
""")


#NOTE: multi-line strings could brim over the indentation although you are inside an if statement!
```