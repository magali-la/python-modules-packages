# import custom module with utility functions in this script
from mypackage import utilities

# this script will call both functions

# call user to input a name for themselves
user_name = input("What is your name?: ")

utilities.greet_user(user_name)

# now get them to submit an integer
try:
    user_num = int(input("Give an integer: "))

    resp = utilities.factorial(user_num)

    print(f"The factorial of {user_num} is {resp}.")
except ValueError:
    print("Sorry that is not a valid integer. Try again.")