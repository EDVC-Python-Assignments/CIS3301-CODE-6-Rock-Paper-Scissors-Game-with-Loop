import os,sys
from mock_input_tests import *
from code_6 import main
import random
options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
user_winning_plays = [[1,2,3],[3,1,2]]
user_loosing_plays = [[1,2,3],[2,3,1]]

def check_if_file_exists():
    try:
        exists = os.path.exists("code_6.py")
        assert exists == True
    except:
        sys.exit()

def test_user_wins_in_three_attempts():
    check_if_file_exists()
    attempts = 3
    user_options = []
    computer_options = []
    for x in range(attempts):
        if x == 0 or x == 2:
            option = random.randint(1,3)
            user_options.append(user_winning_plays[0][option-1])
            computer_options.append(user_winning_plays[1][option-1])
        elif x == 1:
            option = random.randint(1,3)
            user_options.append(user_loosing_plays[0][option-1])
            computer_options.append(user_loosing_plays[1][option-1])  
    
    copy_user_options = user_options.copy()
    set_keyboard_input(copy_user_options)
    main(computer_options)
    output = get_display_output()

    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "The game will decide the winner when a player wins 2 out of 3 games",
        "\nGame 1 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You won! {options_dictionary[user_options[0]]} beats {options_dictionary[computer_options[0]]}",
        "\nGame 2 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You lose! {options_dictionary[computer_options[1]]} beats {options_dictionary[user_options[1]]}",
        "\nGame 3 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You won! {options_dictionary[user_options[2]]} beats {options_dictionary[computer_options[2]]}",
        "\nUser beats computer!"
    ]

def test_user_wins_in_two_attempts():
    check_if_file_exists()
    attempts = 3
    user_options = []
    computer_options = []
    for x in range(attempts-1):
        option = random.randint(1,3)
        user_options.append(user_winning_plays[0][option-1])
        computer_options.append(user_winning_plays[1][option-1])       

    copy_user_options = user_options.copy()
    set_keyboard_input(copy_user_options)
    main(computer_options)
    
    output = get_display_output()
    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "The game will decide the winner when a player wins 2 out of 3 games",
        "\nGame 1 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You won! {options_dictionary[user_options[0]]} beats {options_dictionary[computer_options[0]]}",
        "\nGame 2 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You won! {options_dictionary[user_options[1]]} beats {options_dictionary[computer_options[1]]}",
        "\nUser beats computer!"
    ]


def test_user_looses_in_three_attempts():
    check_if_file_exists()
    attempts = 3
    user_options = []
    computer_options = []
    for x in range(attempts):
        if x == 0 or x == 2:
            option = random.randint(1,3)
            user_options.append(user_loosing_plays[0][option-1])
            computer_options.append(user_loosing_plays[1][option-1])
        elif x == 1:
            option = random.randint(1,3)
            user_options.append(user_winning_plays[0][option-1])
            computer_options.append(user_winning_plays[1][option-1])          

    copy_user_options = user_options.copy()
    set_keyboard_input(copy_user_options)
    main(computer_options)
    
    output = get_display_output()
    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "The game will decide the winner when a player wins 2 out of 3 games",
        "\nGame 1 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You lose! {options_dictionary[computer_options[0]]} beats {options_dictionary[user_options[0]]}",
        "\nGame 2 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You won! {options_dictionary[user_options[1]]} beats {options_dictionary[computer_options[1]]}",
        "\nGame 3 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You lose! {options_dictionary[computer_options[2]]} beats {options_dictionary[user_options[2]]}",
        "\nComputer beats user!"
    ]

def test_user_looses_in_two_attempts():
    check_if_file_exists()
    attempts = 3
    user_options = []
    computer_options = []
    for x in range(attempts-1):
        option = random.randint(1,3)
        user_options.append(user_loosing_plays[0][option-1])
        computer_options.append(user_loosing_plays[1][option-1])
     
    copy_user_options = user_options.copy()
    set_keyboard_input(copy_user_options)
    main(computer_options)
    
    output = get_display_output()
    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "The game will decide the winner when a player wins 2 out of 3 games",
        "\nGame 1 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You lose! {options_dictionary[computer_options[0]]} beats {options_dictionary[user_options[0]]}",
        "\nGame 2 - Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You lose! {options_dictionary[computer_options[1]]} beats {options_dictionary[user_options[1]]}",
        "\nComputer beats user!"
    ]
