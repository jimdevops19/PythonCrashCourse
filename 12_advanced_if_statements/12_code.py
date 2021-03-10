#Advanced If Statements

#Expressions could be merged with some special keywords like **and**, **or** and it could add more complexity to our If statements


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


