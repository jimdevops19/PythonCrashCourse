# Formatted Strings:
## Formatted Strings helps us to write human readable print sentences, by the possiblity to refer to our variables' values within the provided string

```python 
#We need to use f letter before opening the string quotes (single or double)
current_year = 2021
print("Current year is", current_year, ". Next year is", current_year + 1) # Bad Example
print(f"Current year is {current_year}. Next year is {current_year + 1}") # Good Example
```

## Exercise:

###  Insert those variables inside a formatted string, describe the print sentence the way you'd like
```python
favorite_language = "Python"
platform = "Youtube"
channel_name = "JSC"
```

### Answer:
```python
#We need to write some print lines starting with f letter before the single/double quotes
print(f"My favorite language now is {favorite_language}")
print(f"I learn about this language on {platform}")
print(f"The course I take now is on the channel of: {channel_name}")
```