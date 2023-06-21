import random



def goalCheck(computerChoice, userChoice, score, gkScore):
    """
    Checks the user input against the randomized computer choice
    If they are equal the penalty kick was saved
    If they are not equal penalty kick was scored
    """
    if computerChoice == userChoice:
        gkScore += 1
        print("The goalkeeper has saved your attempt!\n")
    else:
        score += 1
        print("You scored!\n")
    print("Goalkeeper score is " + str(gkScore))
    print("Your score is " + str(score))
    return score, gkScore



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
    gkScore = 0
    score = 0
    options = ["left", "right", "middle"]
    print("Welcome to the penalty shootout first to 5\n")

    while score < 5 and gkScore < 5:
        while True:
            print("Please choose where you would like to shoot your penalty")
            print("Data should only contain: left, right, or middle")
            print("Example: middle\n")
                
            userChoice = input("Enter your answer here: ")

            if validate_user_choice(userChoice):
                break

        computerChoice = random.choice(options)
        score, gkScore = goalCheck(computerChoice, userChoice, score, gkScore)
        print()
    if score == 5:
        print("Congrats you won! With a score of ", score)
    else:
        print("Game Over! The goalkeeper won with a score of", gkScore)



main()