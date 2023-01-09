import random
import tkinter as tk


class GameOfLife:
    def __init__(self):
        """
        Initializes the game by creating a window and canvas with tkinter,
        creating the board array, creating the cells array,
        and calling the screen_update method in a loop.
        """

        # Create the Tkinter window and set its properties
        self.window = tk.Tk()
        random.seed()

        # screen_size X screen_size
        self.screen_size = 600

        # screen size must be divisible by board size
        self.board_size = 60

        # Dimension of one cells
        self.cell_size = self.screen_size / self.board_size

        # number of "alive" cells at the beginning
        self.cells = 600
        # Should be less than board_size^2 or ValueError("Sample larger than
        # population or is negative") Default Conwaya (23/3)

        self.stay_pattern, self.born_pattern = "23", "3"
        # Firstly amount of "alive" neighbors that the cell doesn't die
        # Secondly the number of "alive" neighbors that the dead cell comes
        # to life You can take more patterns here:
# https://pl.wikipedia.org/wiki/Gra_w_%C5%BCycie#Modyfikacje_gry_w_%C5%BCycie

        # Stay pattern -> how much you need to be around to survive
        self.stay = [int(x) for x in
                     self.stay_pattern]

        # Born pattern -> how much you need to come to life
        self.born = [int(x) for x in
                     self.born_pattern]

    def play(self):
        """
        Sets the window title, size, and resizability,
        creates the Tkinter canvas and sets its properties,
        initializes the board_array attribute as a 2D array of all False values,
        fills the board_array with a random selection of "alive" cells,
        initializes the cells_array attribute as a 2D array of Tkinter rectangle
        objects representing the cells on the canvas, updates the screen to show
        the initial state of the board, and starts the Tkinter event loop.
        :return:
        """
        # Set the window title
        self.window.title("Game of Life")

        # Set the window size
        self.window.geometry(str(self.screen_size) + "x" + str(
            self.screen_size))

        # Disable resizing of the window
        self.window.resizable(width=False,
                              height=False)

        # Create the Tkinter canvas and set its properties
        self.canvas = tk.Canvas(self.window, width=self.screen_size,
                                height=self.screen_size)

        # Pack the canvas into the window
        self.canvas.pack()

        # Initialize the board_array attribute as a 2D array of all False values
        self.board_array = [[False for _ in range(self.board_size)] for _ in
                            range(
                                self.board_size)]

        # Fill the board_array with a random selection of "alive" cells
        self.create_board_array()

        # Initialize the cells_array attribute
        # as a 2D array of Tkinter rectangle
        # objects representing the cells on the canvas
        self.cells_array = [
            [self.canvas.create_rectangle(x * self.cell_size,
                                          y * self.cell_size,
                                          (x + 1) * self.cell_size,
                                          (y + 1) * self.cell_size,
                                          fill="black") for x in
             range(self.board_size)]
            for y in range(self.board_size)]

        # Update the screen to show the initial state of the board
        self.screen_update()

        # Start the Tkinter event loop
        self.window.mainloop()

    def create_board_array(self):
        """
        Method to initialize the board_array with
        a random selection of "alive" cells
        :return:
        """

        # Take a random sample of cells from the range
        # of possible cells (0 to board_size * board_size - 1)
        for number in random.sample(range(self.board_size * self.board_size),
                                    self.cells):
            # Set the value at the corresponding
            # indices in the board_array to True
            self.board_array[number % self.board_size][
                number // self.board_size] = True

    def screen_update(self):
        """
        Method to update the screen based on the current state of the
        board_array
        :return:
        """

        # Iterate through the cells in the board_array
        for x in range(self.board_size):
            for y in range(self.board_size):

                # If the cell is "alive", set its color to green.
                # If not, set it to black.
                if self.board_array[x][y]:
                    self.canvas.itemconfig(self.cells_array[x][y], fill="green")
                else:
                    self.canvas.itemconfig(self.cells_array[x][y], fill="black")

        # Create a copy of the board_array to be modified
        update_cells_array = [[False for _ in range(self.board_size)] for _ in
                              range(self.board_size)]

        # Iterate through the cells in the board_array
        for x in range(self.board_size):
            for y in range(self.board_size):

                # Calculate the number of "alive" neighbors for the current cell
                neighbors = self.sum_nearest_neighbors(x, y)

                # If cell doesn't alive -> check amount of nearest
                # neighbors in born pattern(By default (3))
                # If cell is alive -> check amount of nearest
                # neighbors in stay pattern (By default (2, 3))
                if not self.board_array[x][y]:
                    if neighbors in self.born:
                        update_cells_array[x][y] = True
                else:
                    if neighbors in self.stay:
                        update_cells_array[x][y] = True
        self.board_array = update_cells_array.copy()
        self.window.after(50, self.screen_update)

    def sum_nearest_neighbors(self, x, y):
        """
        Counts the number of live neighbors for a given cell
        :param x:
        :param y:
        :return:
        """
        y_up = 0 if (y + 1) == self.board_size else (y + 1)
        x_right = 0 if (x + 1) == self.board_size else (x + 1)
        y_down = (self.board_size - 1) if (y - 1) == -1 else (y - 1)
        x_left = (self.board_size - 1) if (x - 1) == -1 else (x - 1)

        # Sum of up cells
        sum_of_neighbors = int(self.board_array[x_left][y_up]) + int(
            self.board_array[x][y_up]) + int(
            self.board_array[x_right][y_up])

        # Sum of middle cells
        sum_of_neighbors += int(self.board_array[x_left][y]) + 0 + int(
            self.board_array[x_right][y])

        # Sum of down cells
        sum_of_neighbors += int(self.board_array[x_left][y_down]) + int(
            self.board_array[x][y_down]) + int(
            self.board_array[x_right][y_down])
        return sum_of_neighbors


apl = GameOfLife()
apl.play()