#Python Hide Credit Card Number Exercise

#Write a program that will behave like a stored credit card on the internet, first 12 digits hidden and the last 4 displayed


#Function should replace the first 12 digits
#Of the given number with *
#And display only the last 4 digits
#Final format: **** **** **** 3456


def hide_card(card_number):
    last_four_digits = card_number[-4:]
    return f'**** **** **** {last_four_digits}'

my_card = hide_card('1234567890123456')
print(my_card)


#Addition to a challenge:
#If we want to handle multiple credit cards in this function, what we can do?

def hide_cards(card_numbers):
    cards_list = [] # We create this empty list to fill in items throughout the for loop execution
    for card_number in card_numbers:
        last_four_digits = card_number[-4:] # This will bring the last_four_digits for each card_number
        formatted_credit_card = f"**** **** **** {last_four_digits}" # This will format the cred
        cards_list.append(formatted_credit_card)

    return cards_list

my_card = hide_cards(['1234567890123456','9876543210987654','1594789812345678'])
print(my_card)