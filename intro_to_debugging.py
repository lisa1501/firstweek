# Syntax errors are often caused by things such as:
# missing a keyword
# missing a colon
# missing the end of a brace, like ), }, ], etc
# misspelling something
# accessing a list or dictionary with the wrong syntax
# unmatching indentation levels
# mixed-use of tabs or spaces

# Runtime Erros
# dividing by zero
# performing an operation on incompatible types
# using an identifier which has not been defined
# accessing a list element, dictionary value or object attribute which doesn’t exist
# trying to access a file which doesn’t exist

# Logical Errors
# using the wrong variable name
# incorrect indentation
# not having the correct conditional checks
# off-by-one errors 

# def addition():
#     num1 = 2
#     num2 = 3
#     print(num1+num2)

# add_together()

# def addition():
#     num1 = input("Enter a number")
#     num2 = input("Enter another number")
#     print(num1+num2)
# addition()

# def multiply():
# num1 = 2
# num2 = 2
# print(num1*num2)
# multiply()
# 

# print(str([True, 0, 55.55]))


# def sing_happy_birthday(name):
#     print("Happy birthday to you")
#     print("Happy birthday to you")
#     print(f"Happy birthday, dear {name}")
#     print("Happy birthday to you")
# sing_happy_birthday("Melinda")
# sing_happy_birthday("Kerry")

# def get_daily_special(todays_date):
#     current_season = get_season(todays_date)

#     if current_season == "Spring":
#         special = "Eggplants"
#     elif current_season == "Summer":
#         special = "Blueberries"
#     elif current_season == "Fall":
#         special = "Sweet Potatoes"
#     else:
#         specail = "Oranges"

#     day_of_week = get_day_of_week(todays_date)

#     if day_of_week == "Saturday" or day_of_week == "Sunday":
#         specail = f"Weekend {special}"

#     return special

# get_daily_special(todays_date)


# def compare_alphabetically(num1,num2):
#     return num1*3
#     return num2+3


# value_1=compare_alphabetically(4,6)    
# print(value_1)

# def is_number_odd(num, message):
#     if num % 2 != 0:
#         print(f"The number passed in ({num}) is odd!")
#         return True
#     print(message)
#     return False

# is_number_odd(5, "This message will never print, because 5 is odd, and the function will return before printing message")
# is_number_odd(8, "This message will print, because the function does not hit a return statement before printing this message")


def display_breakfast():
    breakfast_message = "My breakfast today is an apple"
    print(breakfast_message)

display_breakfast()
print("Let's try to access the value of breakfast_message outside of the display_breakfast function:")
print(f"The value of breakfast_message is {breakfast_message}")