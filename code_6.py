import random

def get_computer_plays(computer_option = None):
   computer_plays =[]
   if computer_option is None:
      for x in range(3):
         computer_plays.append(random.randint(1,3))
      return computer_plays
   else:
      return computer_option

def main(computer_option = None):
   options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
   computer_plays = get_computer_plays(computer_option)
   print("\nWelcome to the Game of Rock, Paper Scissors")
   print("The game will decide the winner when a player wins 2 out of 3 games")
   user_wins = 0
   computer_wins = 0
   game_number = 0
   #Your code starts BELOW this line

   
    
# Do not remove the lines below
if __name__ == "__main__":
    main()
