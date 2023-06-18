import random


print("--------------------")
print("")
options = ["left", "right", "middle"]
computerChoice = random.choice(options)

userChoice = input("Take the penalty choose: left, right or middle: ")





def goalCheck():
    if computerChoice == userChoice:
        print("The goalkeeper has saved your attempt!")
    else:
        print("You scored!")

def validate_user_choice():
    try

def main():
    goalCheck()

main()


    