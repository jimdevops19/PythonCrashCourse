# Python Pythagoras Exercise
## Write a function that will accept three parameters, that will check if given combo of numbers apply the pythagoras theory (3,4,5 applies, because 3 ** 2 + 4 ** 2 = 5 ** 2)
```python 
#Print to the user if the given three numbers
#Apply the Pythagoras formula
# a ** 2 + b ** 2 = c ** 2
def is_pyth_triple(a, b, c):
    num_ab = a ** 2 + b ** 2
    num_c = c ** 2
    if num_ab == num_c:
        print(f"The combination of:{a},{b},{c} supports pyth law!")
    else:
        print(f"The combination of:{a},{b},{c} does not support pyth law!")

is_pyth_triple(3, 4, 5)
is_pyth_triple(5,6,7)
```