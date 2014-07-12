from Player import Player
from Board import Board
import turtle

# Initialize the window for the game.
wn = turtle.Screen()
wn.screensize(339, 296)
wn.setup(width=350, height=300, startx=140, starty=None)
wn.bgpic("tictactoe.gif")

# Initialize Players and Board
p1 = Player()
p2 = Player()
board = Board()
        
def get_next_turn(player):
    if player is None:
        return p1
    if player == p1:
        return p2
    if player == p2:
        return p1

def game():
    endGame = False
    player = None

    while endGame == False:
        player = get_next_turn(player)
        move = raw_input("%s's move: " % player.name)

        # Conditions to ensure the user does not try to break the game!
        while True:
            try:
                int(move)
                if int(move) < 10 and int(move) > 0:
                    if board.tile[int(move)] == None:
                        board.tile[int(move)] = player
                        break
                    else:
                        move = raw_input("Please enter a valid move: ")
                else:
                    move = raw_input("Please enter a valid move: ")
            except:
                move = raw_input("Please enter a valid move: ")

        player.move_token(int(move))
        player.draw_shape()
        if board.check_victory(player) is True \
                or board.check_tie() is True:
            endGame = True
        
game()
wn.exitonclick()
