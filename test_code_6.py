import os,sys
from mock_input_tests import *
from code_6 import main
import random

def check_if_file_exists():
    try:
        exists = os.path.exists("code_6.py")
        assert exists == True
    except:
        sys.exit()

def test_user_wins_in_three_attempts():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
    user_winning_plays = [[1,2,3],[3,1,2]]
    user_loosing_plays = [[1,2,3],[2,3,1]]
    attempts = 3
    user_options = []
    computer_options = []
    for x in range(attempts):
        if x == 0 or x == 2:
            option = random.randint(1,3)
            user_options.append(user_winning_plays[0][option])
            user_options.append(user_winning_plays[1][option])
        elif x == 1:
            option = random.randint(1,3)
            user_options.append(user_loosing_plays[0][option])
            user_options.append(user_loosing_plays[1][option])          

    set_keyboard_input([user_options])
    main(computer_options)
    
    output = get_display_output()

    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "The game will decide the winner when a player wins 2 out of 3 games",
        "Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You won! {options_dictionary[user_option]} beats {options_dictionary[computer_option]}"
    ]

def test_user_wins_in_two_attempts():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}


def test_user_looses():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}

def test_user_ties():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}