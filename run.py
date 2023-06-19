import random



def goalCheck(computerChoice, userChoice, score):
    if computerChoice == userChoice:
        print("The goalkeeper has saved your attempt!")
    else:
        print("You scored!")
        



def validate_user_choice(value):
    try:
        if value not in ["left", "right", "middle"]:
            raise ValueError(
                f"Wrong value submitted you provided {value}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True



def main():
    score = 0
    options = ["left", "right", "middle"]
    computerChoice = random.choice(options)
    for i in range(0,5):
        while True:
            print("Please choose where you would like to shoot your penalty")
            print("Data should only contain: left, right, or middle")
            print("Example: middle")
            
            userChoice = input("Enter your answer here: \n")

            if validate_user_choice(userChoice):
                print("Data is valid!")
                break
        
        goalCheck(computerChoice, userChoice)

main()


    