# # Practice Question
# # 1. Create a list of six school subjects.
# # Ask the user which of these subjects they don't like.
# # Delete the subject they have chosen from the list
# # before you display the list again.
# from operator import index
#
# school_subjects = {"hindi", "english", "maths", "science", "social", "malayalam"}
# c2 = 0 # try counter
# user_sub = set()
# user_like_sub = set()
# while True:
#     user_sub_text = ''
#     user_response = 'n'
#     if c2 > 0:
#         user_response = input('\nDo you want to add another subject?? (y / n) : ')
#     if user_response.lower() == 'y' or c2 == 0:
#         print("\nSchool subjects :", end=' ')
#         c1 = 1  # display counter
#         for single_sub in school_subjects:
#             print(f'{c1}.{single_sub.title()}', end=' ')
#             c1 += 1
#         user_sub_text = input('\nEnter subjects that you dont like: ')
#         user_sub.add(user_sub_text.lower())
#         print('Subjects you dont like : ', user_sub)
#         c2 += 1
#     elif user_response.lower() == 'n':
#         user_like_sub = school_subjects.difference(user_sub)
#         # print final list
#         c3 = 1 # display counter
#         print("\nSchool subjects you like : ", end=' ')
#         for single_sub in user_like_sub:
#             print(f'{ c3 }.{ single_sub.title() }', end=' ')
#             c3 += 1
#         break # stop
#     else:
#         print('wrong response, enter again')
#
# # 2.a. Write a Python program that prompts the user to enter
# # four three-digit numbers, ensuring through a loop that each
# # number entered is exactly three digits; if an invalid number is entered,
# # the program should ask the user to re-enter the number until it's valid.
# # Once all four numbers are collected, display the list of numbers,
# # showing each number on a separate line.
# # 2.b. Then, prompt the user to enter another three-digit number and check
# # if it matches any number in the list. If a match is found, display the
# # position of the number in the list (starting from 1);
# # otherwise, display the message: "That is not in the list."
#
# number_list = list()
# number_list_limit = 4
# while True:
#     if len(number_list) == number_list_limit:
#         print("\nEntered numbers : ")
#         for single_number in number_list:
#             print(single_number)
#         break
#     user_number = input("Enter a 3 digit number : ")
#     c1 = 0
#     for user_number_digit in user_number:
#         c1 += 1
#     if c1 == 3:
#         if user_number.isdigit():
#             number_list.insert(number_list_limit, int(user_number))
#         else:
#             print("\nEnter a 3 digit number again...")
#     else:
#         print("\nEnter a 3 digit number again...")
# user_num_choice = input("Enter a 3 digit number : ")
# c1 = 0
# for user_number_digit in user_num_choice:
#     c1 += 1
# if user_num_choice.isdigit() and c1 == 3:
#     if int(user_num_choice) in number_list:
#         print(f"Match is found at list position : {number_list.index(int(user_num_choice))+1}")
#     else:
#         print("That is not in the list.")
#
# # 3. Enter a list of ten colours.Ask the user for a starting number between 0 and 4
# # and an end number between 5 and 9. Display the list for those colours between the
# # start and end numbers the user input.
#
# color_list = list()
# color_list_limit = 10
# while True:
#     if len(color_list) == color_list_limit:
#         print("\nEntered Colors : ")
#         print(color_list)
#         break
#     user_color = input("Enter a color : ")
#     if user_color.isalpha():
#         color_list.insert(color_list_limit, user_color.lower())
#     else:
#         print('Enter color again...')
# user_lower_limit_num = user_upper_limit_num = 0
# while True:
#     user_lower_limit = input("\nEnter a starting number between 0 and 4 : ")
#     if user_lower_limit.isdigit() and 0 < int(user_lower_limit) < 4:
#         user_lower_limit_num = int(user_lower_limit)
#         break
#     else:
#         print('Enter starting number again...')
# while True:
#     user_upper_limit = input("\nEnter a end number between 5 and 9 : ")
#     if user_upper_limit.isdigit() and 5 < int(user_upper_limit) < 9:
#         user_upper_limit_num = int(user_upper_limit) - 1
#         break
#     else:
#         print('Enter end number again...')
# print("\nResulting color list:")
# print(color_list[user_lower_limit_num:user_upper_limit_num])
#
# # 4. Ask the user to enter the names of three people they want to invite to a party
# # and store them in a list. After they have entered all three names, ask them
# # if they want to add another. If they do, allow them to add more names until
# # they answer "no". When they answer "no", display how many people they have
# # invited to the party.
#
# party_list = list()
# party_list_limit = 3
# while True:
#     if len(party_list) == party_list_limit:
#         print(f'\nInvited { len(party_list) } People : ')
#         # for i in party_list:
#         #     print(f'{ i } ', end = " ")
#         print(", ".join(party_list), end=' ')
#         print(f'are the { len(party_list) } People invited')
#         break
#     person_name = input("Enter a person you want to invite to the party : ")
#     party_list.insert(party_list_limit+1, person_name.title())
#     print(f'{ person_name }, invited.')
# while True:
#     user_response = input('\nDo you want to invite another person? (yes / no) : ')
#     if user_response == 'no':
#         print('\nFinal party list')
#         print('===========================')
#         # for i in party_list:
#         #     print(f'{i} ', end = " ")
#         print(", ".join(party_list), end=' ')
#         print(f'are the { len(party_list) } People invited')
#         break
#     elif user_response == 'yes':
#         person_name = input("Enter a person you want to invite to the party : ")
#         party_list.insert(len(party_list)+1, person_name.title())
#         print(f'{ person_name }, invited.')
#     else:
#         print('wrong response, enter again')
