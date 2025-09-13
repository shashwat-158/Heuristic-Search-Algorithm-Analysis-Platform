# main.py

# Importing necessary libraries
import pygame
import sys # This lets us close the window

# Initialize Pygame
pygame.init()

# Setup constants
# This makes it easy to change the window size or colors later
WIDTH, HEIGHT = 800, 800
# surface object returned by .set_mode() stored in WIN
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # The actual window
pygame.display.set_caption("Pathfinding Algorithm Visualizer") # The title bar text

# Definining color (using RGB values)
WHITE = (255, 255, 255)
# MORE COLORS FOR THE NODES
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0) # Start node
PURPLE = (128, 0, 128)  # End node
BLACK = (0, 0, 0)       # Barrier node
GREY = (128, 128, 128)  # Grid lines


# ------------------- NODE CLASS -------------------
# This is the blueprint for each square on the grid
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        # These are the actual pixel coordinates on the screen
        self.x = col * width
        self.y = row * width
        self.color = WHITE # Start as a white square
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # --- Methods for checking the state of the Node ---
    def get_pos(self):
        return self.row, self.col

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == PURPLE
    
    # --- Methods for changing the state of the Node ---
    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = PURPLE

    def make_barrier(self):
        self.color = BLACK

    def make_open(self):
        self.color = GREEN # Node is in the "open set"
    
    def make_closed(self):
        self.color = RED # Node has been considered
    
    def make_path(self):
        # A different color for the final path
        self.color = (64, 224, 208) # Turquoise

    # --- The method to draw the Node on the screen ---
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

# ----------------------------------------------------


# makes a 2D list of nodes (grid)
# square grids are made because it is better to show algorithms in simple way 
def make_grid(rows, width):
    grid = []
    # size of each square, floor division for whole number
    gap = width//rows
    # outer loop to add list inside list of grid
    for i in range(rows):
        grid.append([])
        # inner loop to create node and add inside current row list
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


# helper function to draw grid lines
def draw_grid(win, rows, width):
    # calculated size of one square using rows and width of window
    gap = width//rows
    # drawing horizontal lines
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
    # drawing vertical lines
    for j in range(rows):
        pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))


# master function to handle all visual updates
def draw(win, grid, rows, width):
    # wiping window
    win.fill(WHITE)
    # looping through every nodes inside grid
    for row in grid:
        for node in row:
            # telling every node to draw themselves on canvas(win)
            node.draw(win)
    # after drawing all nodes, drawing grid lines on top
    draw_grid(win, rows, width)
    # updating the screen to show the result
    pygame.display.update()

# helper function to give mouse position as rows and cols to grid
def get_clicked_pos(pos, rows, width):
    # calculated size of one square using rows and width of window
    gap = width//rows
    # y coordinate divided by size of square will tell it's inside which row
    row = pos[1]//gap
    # x coordinate divided by size of square will tell it's inside which col
    col = pos[0]//gap

    return row, col

# The Main Application Loop
def main():

    # defining number of rows
    ROWS = 50
    # making grid with number of rows and width of window
    grid = make_grid(ROWS, WIDTH)

    # to store start and end of nodes once they are placed
    start = None
    end = None

    run = True
    while run:
        # drwaing the grid on screen
        draw(WIN, grid, ROWS, WIDTH)
        # This loop is the "ears" of the program. It listens for user actions.
        for event in pygame.event.get():
            # If the user clicks the 'X' button on the window...
            if event.type == pygame.QUIT:
                run = False # ...stop the main loop.

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # mouse click on screen returns tuple(0,0,0) 
                mouse_buttons = pygame.mouse.get_pressed()
                # gives (x,y) coordinate of mouse click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]

                # first value will be 1 on left click
                if mouse_buttons[0]:
                    # Only make it the start node if the end node isn't there yet
                    # AND if the clicked node isn't already the end node.
                    if not start and node != end:
                        start = node
                        start.make_start()
                    # Only make it the end node if the start node already exists
                    # AND if the clicked node isn't already the start node.
                    elif not end and node != start:
                        end = node
                        end.make_end()
                    # Only make it a barrier if it's not the start or end node.
                    elif node != end and node != start:
                        node.make_barrier()
                # If right mouse button was clicked
                elif mouse_buttons[2]:
                    # This is where you'll add the logic to reset nodes
                    node.reset()
                    if node == start:
                        start = None
                    elif node == end:
                        end = None

    # Once the loop is finished, quit the program safely.
    pygame.quit()
    sys.exit()

# This line ensures that the main() function runs only when you execute main.py directly
if __name__ == "__main__":
    main()