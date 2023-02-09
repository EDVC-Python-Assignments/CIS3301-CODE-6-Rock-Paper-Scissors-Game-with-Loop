## CIS3301-CODE6-Rock-Paper-Scissors-Game-with-Loop

In this CODE assignment, you are going to program a simple Rock-Paper-Scissors game. The game **should allow the user to play two out of three games** and the end the program should declare who is the winner. Below is the logic the game should have:

* Rock beats Scissors
* Paper beats Rock
* Scissors beats Paper
* It is a tie when the user and the computer choose the same option. For example Paper vs. Paper
* The program should stop if either of the participants (computer or user) has won 2 out of 3 games

## User prompts

* The user is greeted **ONLY SHOW ONCE**
  + **"\nWelcome to the Game of Rock, Paper Scissors"**
  + **"The game will decide the winner when a player wins 2 out of 3 games"**
* The user is asked for their option
  + **"\nGame number_of_game - Choose from the options below\n"** (replace number_of_game)
  + **"1. Rock"**
  + **"2. Paper"**
  + **"3. Scissors"**
  + **"\nEnter your option:"**
* The following messages should be displayed to the user depending on the draw of the computer
  + Tie: **"It is a tie"**
  + The user wins: **"You win game number_of_game! user_option beats computer_option"** (replace number_of_game, user_option and computer_option)
  + The user loses: **"You lose game number_of_game! computer_option beats user_option"** (replace number_of_game, user_option and computer_option)

* The following messages should be displayed at end of the game
  + The user is the overall winner: **\nUser beats computer!**
  + The computer is the overall winner: **\nComputer beats user!**

## Tip

* Use the dictionary `options_dictionary` to compare your output
* The logic of the game can be implemented using if, elif(s), and else
* One side comparison when implementing the logic is effective. In other words implement the logic focusing in one player.