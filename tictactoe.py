import turtle


# Initialize the turtles and screen for the game.
wn = turtle.Screen()
wn.screensize(339, 296)
wn.setup(width=350, height=300, startx=140, starty=None)
wn.bgpic("tictactoe.gif")

class Player:
    'Player class with a name and a color as a parameter.'
    def __init__(self, name, color, shape):
        # Initialize a dictionary to keep track of co-ordinates to draw
        # These will differ due to how the shapes are drawn!
        Player.o = {1: [-100,65], 2: [0,65], 3: [85,65], \
                        4: [-100,-20], 5: [0,-20], 6: [85,-20], \
                        7: [-100,-100], 8: [0,-100], 9: [85,-100]}
        Player.x = {1: [-140,65], 2: [-45,65], 3: [50,65], \
                        4: [-140,-20], 5: [-45,-20], 6: [50,-20], \
                        7: [-140,-100], 8: [-45,-100], 9: [50,-100]}
        self.name = name
        self.shape = shape
        self.token = turtle.Turtle()
        self.token.speed(0)
        self.token.shape("blank")
        self.token.pensize(4)
        self.token.hideturtle()
        
        # Conditions to ensure the user does not try to break the game!
        while True:
            if color == '':
                color = raw_input("Please enter a valid color: ")
            else:
                break

        while True:
            try:
                self.token.color(str(color))
                break
            except:
                color = raw_input("Please enter a valid color: ")

        while True:
            if self.shape == "x" or self.shape == "o":
                break
            else:
                self.shape = raw_input("Please enter a valid shape: ")
        self.token.up()

    # Drawing a circle token
    def draw_shape(self):
        if self.shape == "o":
            self.token.down()
            for i in range(0, 45):
                self.token.left(15)
                self.token.forward(7)
        if self.shape == "x":
            self.token.setheading(35)
            self.token.down()
            self.token.forward(100)
            self.token.up()
            self.token.setheading(270)
            self.token.forward(60)
            self.token.setheading(140)
            self.token.down()
            self.token.forward(90)

    # Invoke a key press (1-9) according to the board.
    def move_token(self, location):
        if self.shape == "x":
            coords = Player.x[location]
        if self.shape == "o":
            coords = Player.o[location]
        self.token.up()
        self.token.home()
        self.token.goto(coords[0], coords[1])


# Player 1
name = raw_input("Enter Player One's Name: ")
color = raw_input("Enter %s's Color: " % name)
shape = raw_input("Enter %s's Shape: " % name)
p1 = Player(name, color, shape)

# Player 2
name = raw_input("Enter Player Two's Name: ")
color = raw_input("Enter %s's Color: " % name)
shape = raw_input("Enter %s's Shape: " % name)
p2 = Player(name, color, shape)

# Victory Message Turtle
message = turtle.Turtle()
message.hideturtle()
message.up()
message.goto(-50,-130)


# Initialize the board with a list to keep track of moves
# Not indexing by 0 to make the layout 'simple'.
board = [0] * 10    

def check_victory(playerNum):
    counter = 0
    if board[1] == playerNum:
        if board[5] == playerNum:
            if board[9] == playerNum:
                return playerNum
        if board[4] == playerNum:
            if board[7] == playerNum:
                return playerNum
        if board[2] == playerNum:
            if board[3] == playerNum:
                return playerNum
    if board[4] == playerNum:
        if board[5] == playerNum:
            if board[6] == playerNum:
                return playerNum
    if board[7] == playerNum:
        if board[8] == playerNum:
            if board[9] == playerNum:
                return playerNum
        if board[5] == playerNum:
            if board[3] == playerNum:
                return playerNum
    if board[2] == playerNum:
        if board[5] == playerNum:
            if board[8] == playerNum:
                return playerNum
    if board[3] == playerNum:
        if board[6] == playerNum:
            if board[9] == playerNum:
                return playerNum
    for i in board:
        if board[i] != 0:
            counter += 1
    if counter == 9:
        return 3
    return 0

def victory(player):
    if player == 3:
        message.write("Cats Game!")
        print "Cats Game! \nThe game has ended. Please click on the window to close the game."
    else:
        message.write("%s Wins!" % player.name)
        print "%s wins! \nThe game has ended. Please click on the window to close the game." % player.name
        
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
                    if board[int(move)] == 0:
                        board[int(move)] = which_player
                        break
                    else:
                        move = raw_input("Please enter a valid move: ")
                else:
                    move = raw_input("Please enter a valid move: ")
            except:
                move = raw_input("Please enter a valid move: ")

        player.move_token(int(move))
        player.draw_shape()
        winner = check_victory(which_player)
        if winner == which_player:
            victory(player)
            break       
        if winner == 3:
            victory(3)
            break

game()
wn.exitonclick()
