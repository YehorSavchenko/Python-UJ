#Game of Life
- The `GameOfLife` class is a representation of the classic game **"Conway's Game of Life"** using the Tkinter library.

    The class has the following attributes:
    - `window`: A Tkinter window object that will be used to display the game. 
    - `canvas`: A Tkinter canvas object that will be used to display the cells of the game. 
    - `board_array`: A two-dimensional array that represents the state of the cells on the board. 
Each element in the array is a boolean that is True if the cell is "alive" and False if it is not. 
    - `cells_array`: A two-dimensional array that contains Tkinter rectangle objects that represent the cells on the canvas.

    The class has the following methods:

    - `__init__(self)`: The constructor for the class. It initializes the window, canvas, and cells_array attributes, and calls the create_board_array and screen_update methods. 
    - `create_board_array(self)`: This method initializes the board_array attribute by randomly selecting a specified number of cells to be "alive."
    - `screen_update(self)`: This method updates the colors of the cells on the canvas based on their status in the board_array. It also updates the board_array by applying the rules of the game to each cell. 
    - `sum_nearest_neighbors(self, x, y)`: This method calculates the number of "alive" cells that are adjacent to the cell at the given x and y indices in the board_array.

    In addition to the GameOfLife class, the code also imports the random and tkinter libraries and sets a number of global variables:

    - `screen_size`: An integer representing the size of the window in pixels. 
    - `board_size`: An integer representing the number of cells in the board in each dimension. 
    - `cells`: An integer representing the number of cells that will be initialized as "alive" in the board. 
    - `born`: A tuple of integers representing the number of adjacent "alive" cells that will cause a dead cell to become "alive" in the next generation. 
    - `stay`: A tuple of integers representing the number of adjacent "alive" cells that will cause an "alive" cell to remain "alive" in the next generation. 
    - `cell_size`: An integer representing the size of each cell in pixels.