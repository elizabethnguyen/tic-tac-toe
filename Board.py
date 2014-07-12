import turtle

class Board:
    # Initialize the board with a list to keep track of moves
    # Not indexing by 0 to make the layout 'simple'.
    def __init__(self):
        Board.tile = [0] * 10    

        # Victory Message Turtle
        Board.message = turtle.Turtle()
        Board.message.hideturtle()
        Board.message.up()
        Board.message.goto(-50,-130)

    def check_victory(self, playerNum):
        counter = 0
        if Board.tile[1] == playerNum:
            if Board.tile[5] == playerNum:
                if Board.tile[9] == playerNum:
                    return playerNum
            if Board.tile[4] == playerNum:
                if Board.tile[7] == playerNum:
                    return playerNum
            if Board.tile[2] == playerNum:
                if Board.tile[3] == playerNum:
                    return playerNum
        if Board.tile[4] == playerNum:
            if Board.tile[5] == playerNum:
                if Board.tile[6] == playerNum:
                    return playerNum
        if Board.tile[7] == playerNum:
            if Board.tile[8] == playerNum:
                if Board.tile[9] == playerNum:
                    return playerNum
            if Board.tile[5] == playerNum:
                if Board.tile[3] == playerNum:
                    return playerNum
        if Board.tile[2] == playerNum:
            if Board.tile[5] == playerNum:
                if Board.tile[8] == playerNum:
                    return playerNum
        if Board.tile[3] == playerNum:
            if Board.tile[6] == playerNum:
                if Board.tile[9] == playerNum:
                    return playerNum
        for i in Board.tile:
            if Board.tile[i] != 0:
                counter += 1
        if counter == 9:
            return 3
        return 0

    def victory(self, player):
        if player == 3:
            Board.message.write("Cats Game!")
            print "Cats Game! \nThe game has ended. Please click on the window to close the game."
        else:
            Board.message.write("%s Wins!" % player.name)
            print "%s wins! \nThe game has ended. Please click on the window to close the game." % player.name


