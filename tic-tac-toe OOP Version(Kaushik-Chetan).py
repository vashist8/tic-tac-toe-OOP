class Board:
    def __init__(self):
        # initialise board
        self.__grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



    def display(self):
        for line in self.__grid:
            for column in line:
                if column == 0:
                    print(" . ",end=' ')
                if column == 1:
                    print(" x ",end=' ')
                if column == 2:
                    print(" o ",end=' ')
            print()


    def cell_0(self):

        for line in self.__grid:
            for column in line:
                if column == 0:
                    return True

    def change_cell(self, value):
        while True:
            i = int(input("Line:   "))
            j = int(input("Column: "))

            if i in range(3) and j in range(3) and self.__grid[i][j] == 0:
                self.__grid[i][j] = value
                break

    def check_win(self, value):
        size = len(self.__grid)

        # let us check lines first
        for i in range(0, size):
            # does line i only contain values which match?
            matching_values = [self.__grid[i][j] for j in range(0, size) if self.__grid[i][j] == value]
            if len(matching_values) == size:
                return True

        # let us check columns
        for j in range(0, size):
            # does column j only contain values which match?
            matching_values = [self.__grid[i][j] for i in range(0, size) if self.__grid[i][j] == value]
            if len(matching_values) == size:
                return True

        # let us check the diagonals now
        # First, the diagonal (0,0), (1,1), (2,2) (etc.)
        matching_values = [self.__grid[i][i] for i in range(0, size) if self.__grid[i][i] == value]

        if len(matching_values) == size:
            return True

        # Second, the diagonal (0,2), (1,1), (2,0) (etc.)
        matching_values = [self.__grid[i][size - i - 1] for i in range(0, size) if self.__grid[i][size - i - 1] == value]

        if len(matching_values) == size:
            return True

        # Here we know that the player has not won
        return False


class Player:
    def __init__(self,id):
        self.name = input("enter player's name: ")
        self.id = id









def main():
    # On commence par initialiser une liste bidimensionnelle à 3 lignes et 3 colonnes
    # avec des « 0 » dans chaque case. Cette liste représentera notre plateau de jeu.
    #game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player1 = Player(1)
    player2 = Player(2)
    gameBoard = Board()
    gameBoard.display()
    # Ensuite, pour chacun des joueurs devront être exécutées les actions suivantes :
    # test du fait que l’on puisse poser un pion, si oui pose du pion,
    # affichage du plateau et test de l’éventuelle victoire,
    # sinon on déclare qu’il y a match nul.

    # we start with player 1

    activePlayer = player1

    while True:
        if not gameBoard.cell_0():
            print("The match is a draw -- no one wins")
            break

        # the player plays
        print(activePlayer.name, "plays")
        gameBoard.change_cell(activePlayer.id)

        # we display the game as the player has just filled-in a cell
        gameBoard.display()

        # we check whether the player has won
        if gameBoard.check_win(activePlayer.id):
            print(activePlayer.name, "wins the game!")
            break

        # On fera jouer les joueurs successivement jusqu’à que
        # l’un des deux gagne.
        if activePlayer.id == 1:
            activePlayer = player2
        else:
            activePlayer = player1

    # Here we know that either the match was a draw
    # or one of the two players won
    print("Thank you for playing.")




main()













