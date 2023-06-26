import random
class Player():
    def __init__(self, name=None):
        self.name = name
        self.score = 0


    def validate_username(self):
        """
        Validates the username input

        Returns:
            None
        """
        while True:
            name = input("Enter your name: ").strip()  # Strip leading/trailing spaces

            if not name:
                print("Username cannot be empty. Please try again.\n")
            else:
                self.name = name
                break


    def validate_user_choice(self, value):
        """
        Validated the user input so no wrong answers can be submitted

        Args:
            value (str): The user's input choice.

        Raises:
            ValueError: If the user's input is not a valid choice.

        Returns:
            bool: True if the user's input is valid, False otherwise.
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


def goal_check(computer_choice, user_choice, user, gk_score):
    """
    Checks the user input against the randomized computer choice

    Args:
        computer_choice (str): The computer's randomized choice.
        user_choice (str): The user's choice.
        user (Player): The Player object representing the user.
        gk_score (int): The goalkeeper's score.

    Returns:
        Tuple[int, int]: A tuple containing the updated user score and goalkeeper score.
    """
    if computer_choice == user_choice:
        gk_score += 1
        print("------------------------------------------------------------")
        print("The goalkeeper has saved your attempt!")
        print("------------------------------------------------------------\n")
    else:
        user.score += 1
        print("------------------------------------------------------------")
        print("You scored!")
        print("------------------------------------------------------------\n")
    print("Goalkeeper score is " + str(gk_score))
    print(f"{user.name}'s score is " + str(user.score))
    print("")
    print("--------------------------------------------------------------")
    return user.score, gk_score

def game(user, gk_score):
    """
    Runs the Penalty shootout, first to 5 game.

    Args:
        user (Player): The Player object representing the user.
        gk_score (int): The goalkeeper's score.

    Returns:
        None
    """
    options = ["left", "right", "middle"]
    while user.score < 5 and gk_score < 5:
        while True:
            print("Please choose where you would like to shoot your penalty")
            print("Data should only contain: left, right, or middle")
            print("Example: middle\n")

            user_choice = input("Enter your answer here: ")

            if user.validate_user_choice(user_choice):
                break

        computer_choice = random.choice(options)
        user.score, gk_score = goal_check(computer_choice, user_choice, user, gk_score)
        print()

    if user.score == 5:
        print(f"Congrats, {user.name}! You won with a score of {user.score}")
    else:
        print(f"Game Over! The goalkeeper won with a score of {gk_score}")

def main():
    """
    Run all game functions
    """
    print("--------------------------------------------------------------")
    print("Welcome to the penalty shootout, first to 5.")
    print("--------------------------------------------------------------")
    gk_score = 0
    user = Player()  
    user.validate_username()
    game(user, gk_score)

if __name__ == '__main__':
    main()
