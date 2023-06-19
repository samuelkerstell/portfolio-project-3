import random



def goalCheck(computerChoice, userChoice):
    """
    Checks the user input against the randomized computer choice
    If they are equal the penalty kick was saved
    If they are not equal penalty kick was scored
    """
    if computerChoice == userChoice:
        print("The goalkeeper has saved your attempt!\n")
    else:
        print("You scored!\n")
        


def validate_user_choice(value):
    """
    Validated the user input so no wrong answers can be submitted
    """
    try:
        if value.lower() not in ["left", "right", "middle"]:
            raise ValueError(
                f"Wrong value submitted you provided {value}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True



def main():
    """
    Run all game functions
    """
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
                break
        
        goalCheck(computerChoice, userChoice)

main()


    