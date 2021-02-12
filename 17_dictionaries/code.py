#Dictionaries

#Dictionaries can allow us to store multiple key value pairs under one variable name


#Wrong practice:
friend_name = "Mike"
friend_age = 25
friend_gender = True
friend_weight = 64.5

#The better approach will be to create dictionary,
#Since the variables have something in common (Friend's attributes)
#And this could be noticed because we use a lot of times the prefix of friend when we create those variables

#We create dictionaries by using {} to variable assignment:

friend = {
#   "key" : "value"
    "name" : "Mike",
    "age" : 25,
    "is_male" : True,
    "weight" : 64.5
}
#See the value of some key:
print(friend["name"])
print(friend.get("name"))

#What will happen if we specify a non existing key ?
print(friend["is_female"]) # Will crash the program if you mismatched the key name
print(friend.get("is_female")) # Will try to find the key, and return the attached value, if does not find, will NOT crash your program, but will show - None

#This could be one more example for a dictionary:

number_to_letter = {
    1 : "a",
    2 : "b",
    3 : "c"
}
print(number_to_letter[1])
#It is important to understand that there is no MUST for the key to be a string, although the best practice would be to have your keys as strings usually, reasons:
#  Integers might be confusing with indexing (what we learned with lists)
#  It feels more descriptive and more human-readable when you have the key as string

#Like in our cell-phones, in Contacts, we don't attach phone numbers to names, we attach names to phone numbers, just a cleaner look.