# Penalty shootout, first to 5

## Welcome!
[View the live project here](https://penalty-shootout-first-to-5-21972da03e60.herokuapp.com)

Penalty Shootout, first to 5 is a simple Python game where you compete against a computer goalkeeper in a penalty shootout. The objective of the game is to score more goals than the goalkeeper. The game follows a "first to 5" format, where the first player to score 5 goals wins the game.

![Different screen sizes](docs/images/amiresponsive.png)

# How to play
  1. The objective is to score more goals than the computer-controlled goalkeeper.
  2. The game follows a "first to 5" format, meaning the first player to score 5 goals wins.
  3. You will be prompted to choose where you want to shoot your penalty: left, right, or middle.
  4. Enter your choice by typing it in the provided input field.
  5. If your input is not one of the valid options (left, right, or middle), you will receive an error message and can try again.
  6. After you make your choice, the computer-controlled goalkeeper will also make a random decision.
  7. If your shot direction matches the goalkeeper's save, it will be considered a saved penalty.
  8. If your shot direction differs from the goalkeeper's save, it will be counted as a scored goal.
  9. The game keeps track of both your score and the goalkeeper's score.
  10. The process continues until either you or the goalkeeper reaches a score of 5.
  11. If you reach a score of 5 first, you will be declared the winner.
  12. If the goalkeeper reaches a score of 5 first, the game ends, and you lose.
  13. The final result will be displayed, indicating whether you won or lost.
  14. Enjoy the game and strive to become the penalty shootout champion by outscoring the goalkeeper!

# Features

## Existing Features

* ### User Input
  * The user can input where they would like to shoot.

![Screenshot of the navigation bar.](readme-images/header.png)

* ### Random goalkeeper save generation
  * The computer randomly chooses in which direction to save.

* ### Score System
  * A user score system to track the user score.
  * A goalkeeper score system to track the goalkeeper score.

* ### Input validation and error-checking
  * The game only accepts specific input choices. The valid options are "left," "right," or "middle" representing the directions to shoot the penalty. Any other input will trigger an error message.
  * The input validation is case-insensitive, meaning that both uppercase and lowercase variations of the valid choices are accepted. For example, "LEFT," "Left," and "left" will all be considered as valid inputs.
  *  If the user provides an invalid input, an error message is displayed, informing them of the incorrect input and prompting them to try again.



## Future Features
* ### Introduce Difficulty Levels:
   * Categorize questions into difficulty levels such as Easy, Medium, and Hard.
   
# Testing


## Testing User Stories

| `Goals` | `How Are They Achieved?` |
| ----- | ---------------------- |
| `First time visitors` | |
| Understand what the website is and how to play the quiz. | The How to play container gives the user a good understanding of what the site is about. |
| Expand their knowledge of the Premier League.  | By playing the quiz and learning from their mistakes. |
| Convert into returning visitors.       | By providing an engaging and valuable experience. |
| `Returning Visitors`   |
| To come back and play more quiz. | Provide frequent updates to the quiz content, including new questions, topics, or themed quizzes. |
| `Admin User`           |
| Updating the quiz and difficulty.| Adding more quizzes and introducing different difficulty levels. |

## Full Testing
Full testing was performed on the following devices:
* PC:
  * Desktop PC
* Laptop:
  * Macbook Air 2021 13.6-inch screen
* Mobile Devices:
  * iPhone 13

Desktop PC tested the site using the following browsers:
* Google Chrome
* Opera
* Firefox

The Apple devices tested the site using the following browsers:
* Safari
* Google Chrome


I've confirmed that the site is responsive and looks good on different screen sizes.

| `Feature` | `Expected Outcome` | `Testing Performance` | `Result` | `Pass/Fail`|
| ----------|--------------------|-----------------------|----------|------------|
| `Header`  | |
| Logo               | When clicked the user will be redirected to the Home Page  | Clicked Logo  |  Redirected to the Home Page  | Pass |
|  | | | | |
| `Quiz Container` |  |
| Start Button  | When clicked user will be able to view the first question.  | Clicked on Start button   | First question shows up  | Pass |
| Correct Answer | When clicked user will get instant feedback making the button green     | Clicked on Correct Answer  | Button turns green     | Pass |
| Wrong Answer  | When clicked user will get instant feedback making the button red  | Clicked on Wrong Answer   | Button turns red      | Pass |
| Next Button  | When clicked next question & answers will show up  | Clicked on Next Button   | Next question & answers shows up      | Pass |
| Submit Button  | When clicked your final score will show up  | Clicked on Submit Button   | The final score shows up      | Pass |
| | | | | |
| `Score System` |
| Correct answer | When correct answer is choosen score goes up 1 point | Choosed correct answer | Score goes up 1 point  | Pass |
| Wrong answer | When wrong answer is choosen score stays the same | Choosed wrong answer | Score stays the same  | Pass |
| | | | | |
| `Result Container` |
| Restart Button |When clicked quiz will restart | Clicked Restart Button | Quiz is restarted  | Pass |
| | | | | |



### Bugs
* Score is not updating until the next button is clicked.

#### Solved Bugs
* I could choose the same option every time and always score this happened because computerChoice = random.choice(options) was happening outside of the while loop so it would never randomize a new choice.
Once I added it to the while loop it was randomizing a new choice every time.


## Validation Testing
* PEP8
  * No errors were returned from https://pep8ci.herokuapp.com

![Screenshot of the Lighthouse Pagespeed](readme-images/lighthouse.png)

# Technologies Used

## Frameworks, Libraries & Progams Used
  * [Gitpod](https://gitpod.io) was used for version control system to manage code changes, and the Gitpod terminal to commit those changes to Git and push them to GitHub.
  * [GitHub](https://github.com) was used to store the project code after being pushed from gitpod.
  * [ChatGPT](https://chat.openai.com) was used to improve copyright in the readme.
 ## Languages Used
 * Python

# Deployment
* The site was deployed to Heroku. The steps to deploy are as follows:
  * Fork or clone this respository
  * Create a new app on Heroku
  * Set the build backs to Python and NodeJS in that order
The live link can be found here - [Penalty shootout game](https://penalty-shootout-first-to-5-21972da03e60.herokuapp.com)

# Credits
  * Code Institute for the deployment terminal