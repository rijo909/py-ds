# write a BMI calculator, and after calculating the BMI display
# the user the results in simple terms
user_weight = float(input("Please enter you weight in Kg : "))
user_height = float(input("Please enter you height in meters : "))
if user_weight<=0 or user_height<= 0:
    print("Weight or Height  can't be zero or less")
else:
    user_bmi = float(user_weight/(user_height)**2)
    print("Your bmi is : ", user_bmi)
    if user_bmi<18.5 and user_bmi>=0:
        print("You are under weight")
    elif user_bmi>=18.5 and user_bmi<24.5:
        print("You are noraml weight")
    elif user_bmi>=25 and user_bmi<29.9:
        print("You are over weight")
    elif user_bmi>30:
        print("You are obese")
    else:
        print("Something went wrong, bmi value is invalid")