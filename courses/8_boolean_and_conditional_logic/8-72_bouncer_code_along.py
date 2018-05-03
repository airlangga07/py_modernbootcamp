# ask for age
age = input("How old are you? ")

# 18-21 wristband
# 21+ drink, normal entry
# too young sorry
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("you can enter, but need a wristband!")
    elif age >= 21:
        print("you are good to enter and can drink!")
    else:
        print("You can't come in, little one.")
else:
    print("Please enter your age.")
