# Lists
## Lists allow us to include multiple pieces of information under one variable name.
```python 
#Examples, with indexing:
people = ["Allen", "Michael", "John", "Ben"]
            #0        #1        #2      #3
            #-4       #-3       #-2     #-1

print(people[0]) # first index

print(people[0]) # second index

print(people[0]) # third index

print(people[0]) # fourth index

print(people[-1]) # first from right (last)

print(people[-2]) # second from right

print(people[-3]) # third from right

print(people[-4]) ## fourth from right


#Range indexing, pulling multiple elements
#[<start_index>:<end_index>]
print(people[0:2]) #pull indexes 0 and 1 (not 2 because the last number is always not included in end_index)
print(people[:2]) # pull every index till index number 2 (equal to example above, zero could be ommited)
print(people[1:]) #pull everything starting from index 1, (everything except zero)
```