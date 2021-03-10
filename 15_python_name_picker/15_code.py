#Python Name Picker Exercise

#Write a program that will pick a name from this list randomly


#The chosen name should be deleted from the list
#We might need to use external libraries for this program
#Print a formatted string that will show the chosen element

#Solution:
import random # We use this library to launch random actions


people = ["Allen", "Michael", "John", "Ben"]
chosen_person = random.choice(people) # Will pick one element from the given list
people.remove(chosen_person)
print(f'The chosen person is: {chosen_person}')
print(f'The length of people list: {len(people)}') # Just a line that proves the remove command worked