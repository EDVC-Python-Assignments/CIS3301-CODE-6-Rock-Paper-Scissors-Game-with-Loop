import os,sys
from mock_input_tests import *
from code_5 import main
import random
def check_if_file_exists():
    try:
        exists = os.path.exists("code_5.py")
        assert exists == True
    except:
        sys.exit()

def test_user_wins_with_rock():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
    computer_option = 3
    user_option = 1
    set_keyboard_input([user_option])
    main(computer_option)
    
    output = get_display_output()
    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You won! {options_dictionary[user_option]} beats {options_dictionary[computer_option]}"
    ]

def test_user_wins_with_paper():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
    computer_option = 1
    user_option = 2
    set_keyboard_input([user_option])
    main(computer_option)
    
    output = get_display_output()
    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You won! {options_dictionary[user_option]} beats {options_dictionary[computer_option]}"
    ]

def test_user_wins_with_scissors():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
    computer_option = 2
    user_option = 3
    set_keyboard_input([user_option])
    main(computer_option)
    
    output = get_display_output()
    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You won! {options_dictionary[user_option]} beats {options_dictionary[computer_option]}"
    ]

def test_user_lose_with_rock():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
    computer_option = 2
    user_option = 1
    set_keyboard_input([user_option])
    main(computer_option)
    
    output = get_display_output()
    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You lose! {options_dictionary[computer_option]} beats {options_dictionary[user_option]}"
    ]

def test_user_lose_with_paper():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
    computer_option = 3
    user_option = 2
    set_keyboard_input([user_option])
    main(computer_option)
    
    output = get_display_output()
    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You lose! {options_dictionary[computer_option]} beats {options_dictionary[user_option]}"
    ]

def test_user_lose_with_scissors():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
    computer_option = 1
    user_option = 3
    set_keyboard_input([user_option])
    main(computer_option)
    
    output = get_display_output()
    
    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        f"You lose! {options_dictionary[computer_option]} beats {options_dictionary[user_option]}"
    ]


def test_game_tie_working():
    check_if_file_exists()
    options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
    computer_option = random.randint(1,3)
    user_option = computer_option
    
    set_keyboard_input([user_option])
    main(computer_option)
    output = get_display_output()

    assert output == [
        "\nWelcome to the Game of Rock, Paper Scissors",
        "Choose from the options below\n",
        "1. Rock",
        "2. Paper",
        "3. Scissors",
        "\nEnter your option:",
        "It is a tie"
    ]