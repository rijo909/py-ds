# Ask for the name of somebody the user wants to invite to a party.
# After this, display the message "[name] has now been invited" and
# add 1 to the count. Then ask if they want to invite somebody else.
# Keep repeating this until they no longer want to invite anyone else
# to the party and then display how many people they have coming to the party.

# import os
#
# def clear_console():
#     # Use 'cls' for Windows and 'clear' for Unix-based systems
#     command = 'cls' if os.name == 'nt' else 'clear'
#     os.system(command)

user_friend_count = 1
while_flag_run = True
user_friend = input('Name somebody, you wants to invite to a party : ')
print(user_friend.title(), " has now been invited")
while while_flag_run:
    user_friend_invite_confirm = input('Do you want to continue inviting people to the party? (yes/no) : ')
    if user_friend_invite_confirm.lower() == 'yes':
        user_friend_n = input('Name somebody else, you wants to invite to a party : ')
        print(user_friend_n.title(), " has now been invited")
        user_friend_count += 1
        # clear_console()
    elif user_friend_invite_confirm.lower() == 'no':
        print(f"You have {user_friend_count} people coming to the party")
        while_flag_run = False
    else:
        print("wrong input, please enter again")