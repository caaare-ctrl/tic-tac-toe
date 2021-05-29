from tic_tac_toe import TicTaeToe

ttt = TicTaeToe()
if input("Which Mode would you like to play? Type M for Multiplayer and S for Single Player: ").upper() == "M":
    ttt.mulitplayer()
else:
    ttt.single_player()
