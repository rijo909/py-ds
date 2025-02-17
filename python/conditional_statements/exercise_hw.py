# # Ask the user for their name and their age. Add 1 to their age and display the output [Name]
# # next birthday you will be [new age].
# user_name = input("Enter your name : ")
# user_age = int(input("Enter your age : "))
# print(f"{user_name}, next birthday you will be {user_age+1}")
#
#
# # •	Write a program that will ask for a number of days and then will show how many hours,
# # minutes and seconds are in that number of days.
# day_number = int(input("Enter number of days : "))
# if day_number > 0:
#     day_number_msg = "days"
#     if day_number == 1:
#         day_number_msg = "day"
#     print(f"{day_number} {day_number_msg} is {day_number*24} Hours or {day_number*24*60} Minutes or {day_number*24*60*60} Seconds")
# else:
#     print("days cant' be 0")
#
#
# # •	Ask the user to enter a number that is under 20. If they enter a number that is 20 or more,
# # display the message "Too high", otherwise display "Thank you".
# num1 = int(input("Enter a number : "))
# if (num1 >= 20):
#     print("Too high")
# else:
#     print("Thank you")
#
#
# # •	Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case
# # they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question,
# # display the answer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”.
# # If they did not answer yes-to the first question, display the answer “Enjoy your day”.
#
# user_rain_answer = input("Is it raining? : ")
# if user_rain_answer.lower() == 'yes':
#     user_rain_answer = input("Is it windy? : ")
#     if user_rain_answer.lower() == 'yes':
#         print("It is too windy for an umbrella")
#     else:
#         print("Take an umbrella")
# else:
#     print("Enjoy your day")
#
#
# # •	Ask the user to enter 1, 2 or 3. If they enter a 1, display-the message "Thank you", if they enter a 2,
# # display "Well done", if they enter a 3, display "Correct". If they enter anything else, display "Error message".
#
# user_choice_num = input("Enter number 1,2 or 3 : ")
# if user_choice_num == '1':
#     print("Thank you")
# elif user_choice_num == '2':
#     print("Well done")
# elif user_choice_num == '3':
#     print("Correct")
# else:
#     print("Error message")
#
#
# # •	Ask the user's age. If they are 18 or over, display the message "You can vote", if they are aged 17,
# # display the message "You can learn to drive", if they are 16, display the message "You can buy a lottery ticket",
# # if they are under 16, display the message "You can go Trick-or-Treating".
#
# user_age = int(input("Enter your age : "))
# if user_age >= 18:
#     print("You can vote")
# elif user_age == 17:
#     print("You can learn to drive")
# elif user_age == 16:
#     print("You can buy a lottery ticket")
# elif user_age < 16 and user_age > 0:
#     print("You can go Trick-or-Treating")
# else:
#     print("error in entered age")
#
# # •	Ask the user to enter their first name and then ask them to enter their surname. Join them together
# # with a space between and display the name and the length of whole name
#
# user_first_name = input("Enter your first name : ")
# user_last_name = input("Enter your surname name : ")
# user_full_name = user_first_name + " " + user_last_name
# print(f"You entered your name as : {user_full_name}, length of your name is {len(user_full_name)}")
#
#
# # •	Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask
# # for a starting number and an ending number and then display just that section of the text (remember
# # Python starts counting from 0 and not 1).
# first_nursery_line = input("Enter first line of nursery rhyme : ")
# print(f"length of your first line nursery rhyme is {len(first_nursery_line)}")
# rhyme_start = int(input("Enter start number : "))
# rhyme_end = int(input("Enter end number : "))
# if rhyme_start != 0:
#     rhyme_start-=1
# print(first_nursery_line[rhyme_start:rhyme_end])
#
# # •	Ask the user to enter their first name. If the length of their first name is under five characters,
# # ask them to enter their surname and join them together (without a space) and display the name upper case.
# # If the length of the first name is five or more characters, display their first name in lower case
#
# user_first_name = input("Enter your first name : ")
# if len(user_first_name) < 5:
#     user_surname_name = input("Enter your surname name : ")
#     print(f"{(user_first_name+user_surname_name).upper()}")
# elif len(user_first_name) >= 5:
#     print(f"{(user_first_name).lower()}")