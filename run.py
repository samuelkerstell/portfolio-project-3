import random



class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0

    def validate_user_choice(self, value):
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


def goalCheck(computerChoice, userChoice, user, gkScore):
    """
    Checks the user input against the randomized computer choice
    If they are equal the penalty kick was saved and the goalkeeper gets one point
    If they are not equal penalty kick was scored and the user gets one point
    """
    if computerChoice == userChoice:
        gkScore += 1
        print("------------------------------------------------------------")
        print("The goalkeeper has saved your attempt!")
        print("------------------------------------------------------------\n")
    else:
        user.score += 1
        print("------------------------------------------------------------")
        print("You scored!")
        print("------------------------------------------------------------\n")
    print("Goalkeeper score is " + str(gkScore))
    print(f"{user.name}'s score is " + str(user.score))
    print("")
    print("--------------------------------------------------------------")
    return user.score, gkScore


def main():
    """
    Run all game functions
    """
    print("--------------------------------------------------------------")
    print("Welcome to the penalty shootout, first to 5.")
    print("--------------------------------------------------------------")
    gkScore = 0
    name = input("Enter your name: ")
    user = Player(name)
    options = ["left", "right", "middle"]
    while user.score < 5 and gkScore < 5:
        while True:
            print("Please choose where you would like to shoot your penalty")
            print("Data should only contain: left, right, or middle")
            print("Example: middle\n")

            userChoice = input("Enter your answer here: ")

            if user.validate_user_choice(userChoice):
                break

        computerChoice = random.choice(options)
        user.score, gkScore = goalCheck(computerChoice, userChoice, user, gkScore)
        print()
    if user.score == 5:
        print(f"Congrats, {user.name}! You won with a score of {user.score}")
    else:
        print(f"Game Over! The goalkeeper won with a score of {gkScore}")

if __name__ == '__main__':
    main()
