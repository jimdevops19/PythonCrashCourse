# While True
## We can use the while True to create programs that will run forever.
```python 
#We can also include break statements inside our while loops, to quit while loops
#when we'd like to
budget = 30
sandwich_price = 5

while True:
    print("You bought a sandwich!")
    budget -= sandwich_price
    if budget == 0:
        break

print(budget)
```