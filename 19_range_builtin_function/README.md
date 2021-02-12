# Range Built-in Function
## Range built in function will allow us to generate list of numbers in a given range of numbers
```python 
#Use case:
#range(100) - will generate all INTEGERS from 0,99

#Now we might think here how did it knew to step by 1 each time ?

#This is it's default value.

#We can write more complex ranges by providing those three pieces of information in the following order:

#range(<start>, <stop>, <step>)


#Examples:
a = range(1,10,1) # 0 1 2 3 4 5 6 7 8 9

b = range(1,21,2) # 1 3 5 7 9 11 13 15 17 19

c = range(5,9,1) #  5 6 7 8

#We are curious why the number of <stop> always not included.

#Well, this is because the last number is ALWAYS not included, and we just have to remember it when we use this function

#If we really want to see their values in a given list, then we should convert the result to list, using list() built-in conversion method


print(list(a))
print(list(b))
print(list(c))
```