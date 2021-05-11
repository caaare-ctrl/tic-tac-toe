import os
import random
from time import sleep


def clear():
    os.system('cls')
#Havent made the computer player

class TicTaeToe:
    def __init__(self):
        self.game_on = True
        self.list_of_players = ["1", "2"]

    def checking(self,place,placeholder):
        if place < 9 and place >= 0:
            if type(placeholder[place]) == int:
                return False
            else:
                print("!!ALERT!!The place has been filled please try again!!\n")
                sleep(1)
                return True
        elif place >= 9 or place < 0:
            print("!!!ALERT!!!Your input is invalid. Please try again!! \n")
            sleep(1)
            return True
    def computer_move(self):
        pass

    def show_result(self,placeholder):
        clear()
        print(f"\n {placeholder[0]}  | {placeholder[1]} |  {placeholder[2]}  ")
        print(" --- --- --- ")
        print(f" {placeholder[3]}  | {placeholder[4]} |  {placeholder[5]}  ")
        print(" --- --- --- ")
        print(f" {placeholder[6]}  | {placeholder[7]} |  {placeholder[8]}\n")

    def calculate(self,player_choice_dict):
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

    def start_again(self):
        if input("Want to Try again? Type Y for Yes and N for No\n").upper() == "Y":
            clear()
            self.gameinterface()
            return True
        return False


    def gameinterface(self):
        placeholder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffled = random.sample(self.list_of_players, len(self.list_of_players))
        first_player = shuffled[0]
        second_player = shuffled[1]
        player_choice_dict = {first_player: [], second_player: []}
        count = 1
        print("-------- Welcome to Tic-Tac-Toe! -------- ")
        print(f"Player {first_player} , you should go first!")
        first_player_choice = input(f"          Player {first_player}, X or O?\n").upper()
        if first_player_choice == "X":
            player2 = "O"
        else:
            player2 = "X"

        while self.game_on:
            check = True
            if count % 2 == 1:
                who_to_play = first_player
                symbol = first_player_choice
            elif count % 2 == 0:
                symbol = player2
                who_to_play = second_player
            while check:
                self.show_result(placeholder)
                place = int(input(f"Player {who_to_play}! Please place your {symbol} by typing (1-9)\n")) - 1
                check = self.checking(place, placeholder)

            player_choice_dict[who_to_play].append(place)
            placeholder[place] = symbol
            count += 1

            self.show_result(placeholder)
            if count > 3:
                if self.calculate(player_choice_dict):
                    self.game_on = self.start_again()
                elif count == 10:
                    print("It is a draw!")
                    self.game_on = self.start_again()
            print("Goodbye See you")
