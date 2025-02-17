# 1. Ask the user if it is raining and convert their answer to lower case so it doesn’t matter
# what case they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to
# this second question, display the answer “It is too windy for an umbrella”, otherwise
# display the message “Take an umbrella’. If they did not answer yes to the first question,
# display the answer “Enjoy your day”.
user_choice = input("Is it raining? : ")
if user_choice.lower() == 'yes':
    user_choice2 = input("Is it windy? :")
    if user_choice2.lower() == 'yes':
        print("It is too windy for an umbrella")
    elif user_choice2.lower() == 'no':
        print("Take an umbrella")
else:
    print("Enjoy your day")

# 2. Ask the user to enter their first name. If the length of their first name is under five
# characters, ask them to enter their surname and join them together (without a space)
# and display the name in upper case. If the length of the first name is five or more
# characters, display their first name in lower case.

# user_name = input("Enter your name : ")
# if len(user_name):


# 3. Ask the user to enter a number between 10 and 20. If they enter a value under 10,
# display the message “Too low’ and ask them to try again. If they enter a value above 20,
# display the message “Too high” and ask them to try again. Keep repeating this until they
# enter a value that is between 10 and 20 and then display the message “Thank you” |

# PYTHON QUESTIONS:
# =====================
# 1) Get user input using input("Enter your age:"). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.



# 2) Write a Python program that asks the user to enter their age and
# then determine the price of the movie ticket based on the following age groups:
# Under 3 years old: Free
# 3 to 12 years old: Rs1@
# 13 to 59 years old: Rs15
# 6@ years and older: Rs12



# 3) Write a Python program that asks the user to enter an integer and
# then classify the number based on the following criteria:
# Divisible by 2 and 3: Print “ The number is divisible by both 2 and 3”.
# Divisible by 2 but not by 3: Print “ The number is divisible by 2 but not by 3”.
# Divisible by 3 but not by 2: Print “ The number is divisible by 3 but not by 2”.
# Not divisible by either 2 or 3: Print “ The number is not divisible by either 2 or 3".

