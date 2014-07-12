import turtle

class Board:
    # Initialize the board with a list to keep track of moves
    # Not indexing by 0 to make the layout 'simple'.
    def __init__(self):
        Board.tile = [None] * 10    

        # Victory Message Turtle
        Board.message = turtle.Turtle()
        Board.message.hideturtle()
        Board.message.up()
        Board.message.goto(-50,-130)

    def check_victory(self, player):
        if Board.tile[1] == player:
            if Board.tile[5] == player:
                if Board.tile[9] == player:
                    Board.victory(self,player)
                    return True
            if Board.tile[4] == player:
                if Board.tile[7] == player:
                    Board.victory(self,player)
                    return True
            if Board.tile[2] == player:
                if Board.tile[3] == player:
                    Board.victory(self,player)
                    return True
        if Board.tile[4] == player:
            if Board.tile[5] == player:
                if Board.tile[6] == player:
                    Board.victory(self,player)
                    return True
        if Board.tile[7] == player:
            if Board.tile[8] == player:
                if Board.tile[9] == player:
                    Board.victory(self,player)
                    return True
            if Board.tile[5] == player:
                if Board.tile[3] == player:
                    Board.victory(self,player)
                    return True
        if Board.tile[2] == player:
            if Board.tile[5] == player:
                if Board.tile[8] == player:
                    Board.victory(self,player)
                    return True
        if Board.tile[3] == player:
            if Board.tile[6] == player:
                if Board.tile[9] == player:
                    Board.victory(self,player)
                    return True
        return False

    def check_tie(self):
        counter = 0
        for i in range(0,10):
            if Board.tile[i] is not None:
                counter += 1
        if counter == 9:
            Board.message.write("Cats Game!")
            print "Cats Game! \nThe game has ended. Please click on the window to close the game."
            return True
        else:
            return False

    def victory(self, player):
        Board.message.write("%s Wins!" % player.name)
        print "%s wins! \nThe game has ended. Please click on the window to close the game." % player.name


