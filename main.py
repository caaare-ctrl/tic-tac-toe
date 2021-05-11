import random
import os
from tic_tac_toe import TicTaeToe
def clear():
    os.system('cls')

def whostartthegame(list_of_players):
    list_of_players =  random.sample(list_of_players,len(list_of_players))
    return list_of_players

def show_result(placeholder):
    clear()
    print(f"\n {placeholder[0]}  | {placeholder[1]} |  {placeholder[2]}  ")
    print(" --- --- --- ")
    print(f" {placeholder[3]}  | {placeholder[4]} |  {placeholder[5]}  ")
    print(" --- --- --- ")
    print(f" {placeholder[6]}  | {placeholder[7]} |  {placeholder[8]}\n")

def calculate(player_choice_dict):
    for player, player_choice in player_choice_dict.items():
        if 0 in player_choice:
            if set([1, 2]).issubset(set(player_choice)) or set([4, 8]).issubset(set(player_choice)) or set(
                    [3, 6]).issubset(set(player_choice)):
                print(f"Player {player} Win!!")
                return True
        if 4 in player_choice:
            if set([3, 5]).issubset(set(player_choice)) or set([2, 6]).issubset(set(player_choice)) or set(
                    [1, 7]).issubset(set(player_choice)):
                print(f"Player {player} Win!!")
                return True
        if 8 in player_choice:
            if set([6, 7]).issubset(set(player_choice)) or set([2, 5]).issubset(set(player_choice)):
                print(f"Player {player} Win!!")
                return True
def checking(place,placeholder):
    if place < 9 and place >= 0:
        if placeholder[place] == " ":
            return False
        else:
            print("!!ALERT!!The place has been filled please try again!!\n")
            return True
    elif place >= 9 or place < 0:
        print("!!!ALERT!!!Your input is invalid. Please try again!! \n")
        return True

def gameinterface():
    game_on = True
    shuffled = whostartthegame(["1", "2"])
    print(shuffled)
    player_choice_dict = {"1": [],"2": []}
    placeholder = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    first_player = shuffled[0]
    second_player = shuffled[1]
    print("-------- Welcome to Tic-Tac-Toe! -------- ")
    player1 = input(f"          Player {first_player}, X or O?\n").upper()
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    print(f"Player {first_player} , you should go first")
    count = 1
    while game_on:
        check = True
        if count % 2 == 1:
            who_to_play = first_player
            symbol = player1
        elif count % 2 == 0:
            symbol = player2
            who_to_play = second_player
        while check:
            place = int(input(f"Player {who_to_play}! Please place your {symbol} by typing (1-9)\n")) - 1
            check = checking(place,placeholder)
        player_choice_dict[who_to_play].append(place)
        placeholder[place] = symbol
        count += 1
        show_result(placeholder)
        if count > 3:
            if calculate(player_choice_dict):
                game_on= False
                if input("Want to Try again? Type Y for Yes and N for No\n").upper()=='Y':
                    clear()
                    gameinterface()
            elif count == 10:
                print("It is a draw!")
                game_on = False
                if input("Want to Try again? Type Y for Yes and N for No\n").upper()=="Y":
                    clear()
                    gameinterface()
    print("Goodbye, See you next time")

# gameinterface()

ttt = TicTaeToe()

ttt.gameinterface()
