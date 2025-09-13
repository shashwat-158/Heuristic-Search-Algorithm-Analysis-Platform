# main.py

# Importing necessary libraries
import pygame
import sys # This lets us close the window

# Initialize Pygame
pygame.init()

# Setup constants (variables that won't change)
# This makes it easy to change the window size or colors later
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # The actual window
pygame.display.set_caption("Pathfinding Algorithm Visualizer") # The title bar text

# Define a color (using RGB values)
WHITE = (255, 255, 255)
# ADD MORE COLORS FOR THE NODES
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0) # Start node
PURPLE = (128, 0, 128)  # End node
BLACK = (0, 0, 0)       # Barrier node
GREY = (128, 128, 128)  # Grid lines


# ------------------- NODE CLASS -------------------
# This is the blueprint for each square on the grid
class Node:
    # This is the "constructor" method. It runs every time we create a new Node.
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        # These are the actual pixel coordinates on the screen
        self.x = row * width
        self.y = col * width
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


# The Main Application Loop
# This loop is the "heartbeat" of the program. It runs continuously.
def main():
    run = True
    while run:
        # This loop is the "ears" of the program. It listens for user actions.
        for event in pygame.event.get():
            # If the user clicks the 'X' button on the window...
            if event.type == pygame.QUIT:
                run = False # ...stop the main loop.
        
        # 5. Drawing
        # In each frame, we first fill the background with a color.
        WIN.fill(WHITE)
        
        # Then we update the display to show what we've drawn.
        pygame.display.update()

    # Once the loop is finished, quit the program safely.
    pygame.quit()
    sys.exit()

# This line ensures that the main() function runs only when you execute main.py directly
if __name__ == "__main__":
    main()