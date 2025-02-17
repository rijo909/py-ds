pre_user_name="abc123"
pre_pass_word="p123"

user_name=input("Enter username : ")
pass_word=input("Enter password : ")
if(pre_user_name==user_name and pre_pass_word==pass_word):
    print("Hi Welcome user!")
elif(pre_user_name!=user_name and pre_pass_word==pass_word):
    print("The user id doesnt exist")
elif (pre_user_name == user_name and pre_pass_word != pass_word):
    print("The password entered is wrong")
elif (pre_user_name != user_name and pre_pass_word != pass_word):
    print("The username and password entered is wrong")