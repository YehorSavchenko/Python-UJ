import random
import tkinter as tk


class GameOfLife:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Game of Life")
        self.window.geometry(str(screen_size) + "x" + str(screen_size))
        self.window.resizable(width=False, height=False)
        self.canvas = tk.Canvas(self.window, width=screen_size, height=screen_size)
        self.canvas.pack()
        self.board_array = [[False for _ in range(board_size)] for _ in range(board_size)]
        self.create_board_array()
        self.cells_array = [[self.canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size,
                                                          (y + 1) * cell_size, fill="black") for x in range(board_size)]
                            for y in range(board_size)]
        self.screen_update()
        self.window.mainloop()

    # Initialization of board with "alive" cells
    def create_board_array(self):
        # Take cells from board_size * board_size range
        for number in random.sample(range(board_size * board_size), cells):
            self.board_array[number % board_size][number // board_size] = True

    def screen_update(self):
        for x in range(board_size):
            for y in range(board_size):
                # If cell is "alive" -> green
                # If not -> black
                if self.board_array[x][y]:
                    self.canvas.itemconfig(self.cells_array[x][y], fill="green")
                else:
                    self.canvas.itemconfig(self.cells_array[x][y], fill="black")

        update_cells_array = [[False for _ in range(board_size)] for _ in range(board_size)]
        for x in range(board_size):
            for y in range(board_size):
                neighbors = self.sum_nearest_neighbors(x, y)
                # If cell doesn't alive -> check amount of nearest neighbors in born pattern(By default (3))
                # If cell is alive -> check amount of nearest neighbors in stay pattern (By default (2, 3))
                if not self.board_array[x][y]:
                    if neighbors in born:
                        update_cells_array[x][y] = True
                else:
                    if neighbors in stay:
                        update_cells_array[x][y] = True
        self.board_array = update_cells_array.copy()
        self.window.after(50, self.screen_update)

    def sum_nearest_neighbors(self, x, y):
        y_up = 0 if (y + 1) == board_size else (y + 1)
        x_right = 0 if (x + 1) == board_size else (x + 1)
        y_down = (board_size - 1) if (y - 1) == -1 else (y - 1)
        x_left = (board_size - 1) if (x - 1) == -1 else (x - 1)

        # Sum of up cells
        sum_of_neighbors = int(self.board_array[x_left][y_up]) + int(self.board_array[x][y_up]) + int(
            self.board_array[x_right][y_up])
        # Sum of middle cells
        sum_of_neighbors += int(self.board_array[x_left][y]) + 0 + int(self.board_array[x_right][y])
        # Sum of down cells
        sum_of_neighbors += int(self.board_array[x_left][y_down]) + int(self.board_array[x][y_down]) + int(
            self.board_array[x_right][y_down])
        return sum_of_neighbors


random.seed()
screen_size = 600  # screen_size X screen_size
board_size = 60  # screen size must be divisible by board size
cell_size = screen_size / board_size  # Dimension of one cells
cells = 3601  # number of "alive" cells at the beginning
             # Should be less than board_size^2 or ValueError("Sample larger than population or is negative")
# Default Conwaya (23/3)

stay_pattern, born_pattern = "23", "3"  # Firstly amount of "alive" neighbors that the cell doesn't die
                                        # Secondly the number of "alive" neighbors that the dead cell comes to life
# You can take more patterns here: https://pl.wikipedia.org/wiki/Gra_w_%C5%BCycie#Modyfikacje_gry_w_%C5%BCycie
stay = [int(x) for x in stay_pattern]  # Stay pattern -> how much you need to be around to survive
born = [int(x) for x in born_pattern]  # Born pattern -> how much you need to come to life
apl = GameOfLife()