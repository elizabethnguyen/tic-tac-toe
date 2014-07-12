import turtle

class Player:
    'Player class with a name and a color as a parameter.'
    def __init__(self):
        # Initialize a dictionary to keep track of co-ordinates to draw
        # These will differ due to how the shapes are drawn!
        Player.o = {1: [-100,65], 2: [0,65], 3: [85,65], \
                        4: [-100,-20], 5: [0,-20], 6: [85,-20], \
                        7: [-100,-100], 8: [0,-100], 9: [85,-100]}
        Player.x = {1: [-140,65], 2: [-45,65], 3: [50,65], \
                        4: [-140,-20], 5: [-45,-20], 6: [50,-20], \
                        7: [-140,-100], 8: [-45,-100], 9: [50,-100]}

        self.token = turtle.Turtle()
        self.token.hideturtle()
        self.token.up()

        self.name = raw_input("Enter a Name: ")
  
        # Conditions to ensure the user does not try to break the game!
        self.color = raw_input("Enter %s's Color: " % self.name)

        while True:
            try:
                self.token.color(str(self.color))
                break
            except:
                self.color = raw_input("Please enter a valid color: ")

        while True:
            if self.color == '':
                self.color = raw_input("Please enter a valid color: ")
            else:
                break        

        self.shape = raw_input("Enter %s's Shape: " % self.name)
        while True:
            if self.shape == "x" or self.shape == "o":
                break
            else:
                self.shape = raw_input("Please enter a valid shape: ")
        self.token.speed(0)
        self.token.shape("blank")
        self.token.pensize(4)

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
