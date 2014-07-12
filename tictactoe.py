from Player import Player
from Board import Board
import turtle

# Initialize the turtles and screen for the game.
wn = turtle.Screen()
wn.screensize(339, 296)
wn.setup(width=350, height=300, startx=140, starty=None)
wn.bgpic("tictactoe.gif")

# Initialize Players and Board
p1 = Player()
p2 = Player()
board = Board()
        
def get_next_turn(player):
    if player == 0:
        return 1
    if player == 1:
        return 2
    if player == 2:
        return 1

def game():
    winner = 0
    which_player = 0
    while winner == 0:
        which_player = get_next_turn(which_player)
        move = raw_input("Player %s's move: " % which_player)
        if which_player == 1:
            player = p1
        if which_player == 2:
            player = p2

        # Conditions to ensure the user does not try to break the game!
        while True:
            try:
                int(move)
                if int(move) < 10 and int(move) > 0:
                    if board.tile[int(move)] == 0:
                        board.tile[int(move)] = which_player
                        break
                    else:
                        move = raw_input("Please enter a valid move: ")
                else:
                    move = raw_input("Please enter a valid move: ")
            except:
                move = raw_input("Please enter a valid move: ")

        player.move_token(int(move))
        player.draw_shape()
        winner = board.check_victory(which_player)
        if winner == which_player:
            board.victory(player)
            break       
        if winner == 3:
            board.victory(3)
            break

game()
wn.exitonclick()
