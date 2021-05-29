import os
import random
from time import sleep


def clear():
    os.system('cls')


class TicTaeToe:
    def __init__(self):
        self.game_on = True
        self.list_of_players = ["1", "2"]

    def checking(self, place, placeholder):
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

    def computer_move(self, player_choice_dict):
        player_choice = player_choice_dict["Player"]
        computer_choice = player_choice_dict["Computer"]
        if set([1, 2]).issubset(set(player_choice)) or set([4, 8]).issubset(set(player_choice)) or \
                set([3, 6]).issubset(set(player_choice)):
            if 0 not in computer_choice:
                return 0
        if set([0, 2]).issubset(set(player_choice)) or set([4, 7]).issubset(set(player_choice)):
            if 1 not in computer_choice:
                return 1
        if set([0, 1]).issubset(set(player_choice)) or set([5, 8]).issubset(set(player_choice)) or \
                set([4,6]).issubset(set(player_choice)):
            if 2 not in computer_choice:
                return 2
        if set([0, 6]).issubset(set(player_choice)) or set([4, 5]).issubset(set(player_choice)):
            if 3 not in computer_choice:
                return 3
        if set([3, 5]).issubset(set(player_choice)) or set([2, 6]).issubset(set(player_choice)) or \
                set([1, 7]).issubset(set(player_choice)) or set([0,8]).issubset(set(player_choice)):
            if 4 not in computer_choice:
                return 4
        if set([3, 4]).issubset(set(player_choice)) or set([2, 8]).issubset(set(player_choice)):
            if 5 not in computer_choice:
                return 5
        if set([0, 3]).issubset(set(player_choice)) or set([2, 4]).issubset(set(player_choice)) or \
                set([7, 8]).issubset(set(player_choice)):
            if 6 not in computer_choice:
                return 6
        if set([1, 4]).issubset(set(player_choice)) or set([6, 8]).issubset(set(player_choice)):
            if 7 not in computer_choice:
                return 7
        if set([6, 7]).issubset(set(player_choice)) or set([2, 5]).issubset(set(player_choice)) or \
                set([0, 4]).issubset(set(player_choice)):
            if 8 not in computer_choice:
                return 8
        else:
            remain_choices = list(set([0, 1, 2, 3, 4, 5, 6, 7, 8]) - set(player_choice + computer_choice))
            return random.choice(remain_choices)

    def show_result(self, placeholder):
        clear()
        print(f"\n {placeholder[0]}  | {placeholder[1]} |  {placeholder[2]}  ")
        print(" --- --- --- ")
        print(f" {placeholder[3]}  | {placeholder[4]} |  {placeholder[5]}  ")
        print(" --- --- --- ")
        print(f" {placeholder[6]}  | {placeholder[7]} |  {placeholder[8]}\n")

    def calculate(self, player_choice_dict):
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

    def start_again(self,game_mode):
        if input("Want to Try again? Type Y for Yes and N for No\n").upper() == "Y":
            clear()
            game_mode()
        else:
            print("Goodbye See you")
            return False

    def mulitplayer(self):
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
                who_to_play = second_player
                symbol = player2
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
                    self.game_on = self.start_again(self.mulitplayer)
                elif count == 10:
                    print("It is a draw!")
                    self.game_on = self.start_again(self.mulitplayer)
            print("Goodbye See you")

    def single_player(self):
        placeholder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        first_player = "Player"
        second_player = "Computer"
        player_choice_dict = {first_player: [], second_player: []}
        count = 1
        print("-------- Welcome to Tic-Tac-Toe! -------- ")
        print(f"Player, you should go first!")
        first_player_choice = input(f"          Player {first_player}, X or O?\n").upper()
        if first_player_choice == "X":
            computer = "O"
        else:
            computer = "X"
        while self.game_on:
            check = True
            if count % 2 == 1:
                who_to_play = first_player
                symbol = first_player_choice
                while check:
                    self.show_result(placeholder)
                    place = int(input(f"Player ! Please place your {symbol} by typing (1-9)\n")) - 1
                    check = self.checking(place, placeholder)

            elif count % 2 == 0:
                print("It is Computer Move")
                who_to_play = second_player
                symbol = computer
                place = self.computer_move(player_choice_dict)
            player_choice_dict[who_to_play].append(place)
            placeholder[place] = symbol
            count += 1
            self.show_result(placeholder)

            if count > 3:
                if self.calculate(player_choice_dict):
                    self.game_on = self.start_again(self.single_player)
                elif count == 10:
                    print("It is a draw!")
                    self.game_on = self.start_again(self.single_player)
