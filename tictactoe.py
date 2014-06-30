import turtle

# Initialize the turtles and screen for the game.
wn = turtle.Screen()
wn.screensize(339, 296)
wn.setup(width=350, height=300, startx=140, starty=None)
wn.bgpic("tictactoe.gif")

# Player 1
p1 = turtle.Turtle()
p1.color("blue")
p1.speed(0)
p1.shape("blank")
p1.pensize(4)
p1.hideturtle()
p1.up()

# Player 2
p2 = turtle.Turtle()
p2.color("red")
p2.speed(0)
p2.shape("blank")
p2.pensize(4)
p2.hideturtle()
p2.up()

# Victory Message Turtle
message = turtle.Turtle()
message.color("black")
message.pensize(6)
message.hideturtle()
message.up()
message.goto(-50,-130)

# Initialize the board with a list to keep track of moves
board = [0] * 9

# Initialize a dictionary to keep track of co-ordinates to draw
# These will differ due to how the shapes are drawn!
# P1: CROSS
# P2: CIRCLE
p1Grid = {1: [-100,65], 2: [0,65], 3: [85,65], \
              4: [-100,-20], 5: [0,-20], 6: [85,-20], \
              7: [-100,-100], 8: [0,-100], 9: [85,-100]}
p2Grid = {1: [-140,65], 2: [-45,65], 3: [50,65], \
              4: [-140,-20], 5: [-45,-20], 6: [50,-20], \
              7: [-140,-100], 8: [-45,-100], 9: [50,-100]}

# Drawing a circle token
def draw_circle(player):
    player.down()
    for i in range(0, 45):
        player.left(15)
        player.forward(7)

# Drawing a cross token
def draw_cross(player):
    player.setheading(35)
    player.down()
    player.forward(100)
    player.up()
    player.setheading(270)
    player.forward(60)
    player.setheading(140)
    player.down()
    player.forward(90)
    

# Invoke a key press (1-9) according to the board.
def move_token(player, location):
    if player == p1:
        p1.up()
        p1.home()
        coords = p1Grid[location]
        player.goto(coords[0], coords[1])
    if player == p2:
        p2.up()
        p2.home()
        coords = p2Grid[location]
        player.goto(coords[0], coords[1])

#for i in range(1,10):
#    move_token(p2, i)
#    draw_cross(p2)

#userInput = 5
#while int(userInput) > 0 and int(userInput) < 10:
#    userInput = raw_input("Enter something: ")
#    move_token(p1, int(userInput))
#    draw_circle(p1)

def check_victory(playerNum):
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
    return 0

def victory(player):
    if player == 1:
        message.write("Player One Wins!")
    if player == 2:
        message.write("Player Two Wins!")
    if player == 3:
        message.write("Cats Game!")


def game():
    winner = 0
    while winner == 0:
        playerOne = raw_input("Player 1's move: ")
        move_token(p1, int(playerOne))
        draw_circle(p1)
        board[int(playerOne)] = 1
        winner = check_victory(1)
        if winner == 1:
            victory(1)
            break
        playerTwo = raw_input("Player 2's move: ")
        move_token(p2, int(playerTwo))
        draw_cross(p2)
        board[int(playerTwo)] = 2
        winner = check_victory(2)
        if winner == 2:
            victory(2)
            break

game()
wn.exitonclick()
