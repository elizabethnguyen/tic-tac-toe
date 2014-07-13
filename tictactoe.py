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

# Needs work ...        
def reset_players():
    p1 = Player()
    p2 = Player()
    

def get_next_turn(player):
    if player is None:
        return p1
    if player == p1:
        return p2
    if player == p2:
        return p1

def check_move(move):
    try:
        int(move)
    except:
        return False
    if int(move) < 10 and int(move) > 0:
        if board.tile[int(move)] == None:
            return True
    else:
        return False

# Needs work ...
def play_again():
    response = raw_input("Play again? (y/n): ")
    if str.lower(response) == "y":
        wn.resetscreen()
        board.reset_board()
        reset_players()
        return False
    else:
        return True

def game():
    endGame = False
    player = None

    while endGame == False:
        player = get_next_turn(player)
        move = raw_input("%s's move: " % player.name)

        if check_move(move) is True:
            board.tile[int(move)] = player
        else:
            move = raw_input("Please enter a valid move: ")

        player.move_token(int(move))
        player.draw_shape()
        if board.check_victory(player) is True or board.check_tie() is True:
            endGame = True

game()
wn.bye()
