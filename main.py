import pygame
import time
import random
from searching_algos import *

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
PURPLE = (128, 0, 128)
PINK = (255, 105, 180)
YELLOW = (255, 255, 0)

# Color mapping for each algorithm
algorithm_colors = {
    "BFS": GREEN,
    "DFS": PINK,
    "A*": PURPLE,
    "Dijkstra": BLUE,
    "UCS": YELLOW
}

# Initialize Pygame and screen
pygame.init()
width, height = 800, 950  # Increase height to add space for buttons
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pathfinding Algorithm Visualization")



# Grid dimensions and cell size
rows, cols = 40, 50  # Fewer rows to make the maze shorter
cell_size = width // cols

# Button configuration
buttons = ["BFS", "DFS", "A*", "Dijkstra", "UCS"]
button_width = width // len(buttons) - 20  # Adjust width for better spacing
button_height = 50
button_color = GREY
button_font = pygame.font.SysFont("comicsans", 20)
button_font_color = WHITE

def create_grid(rows, cols):
    return [["empty" for _ in range(cols)] for _ in range(rows)]

def add_obstacles(grid, obstacle_count, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    obstacles_added = 0

    while obstacles_added < obstacle_count:
        x = random.randint(0, rows - 1)
        y = random.randint(0, cols - 1)
        if (x, y) != start and (x, y) != goal and grid[x][y] != "obstacle":
            grid[x][y] = "obstacle"
            obstacles_added += 1
    return grid

def draw_grid(screen, grid, cell_size):
    screen.fill(TURQUOISE)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if grid[x][y] == "obstacle":
                pygame.draw.rect(screen, RED, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect, 1)
    pygame.display.update()

def visualize_step(screen, node, cell_size, color):
    x, y = node
    pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
    pygame.display.update()
    time.sleep(0.05)

def visualize_path(screen, path, cell_size, color):
    for node in path:
        visualize_step(screen, node, cell_size, color)

def display_path_info(algorithm_name, path):
    """Display path info in the console."""
    if path:
        print(f"{algorithm_name} Path:")
        print(f"Start: {path[0]}")
        print("Path coordinates:")
        for step in path:
            print(step)
        print(f"Goal: {path[-1]}")
        print(f"Number of steps: {len(path)}")
        print("=" * 40)
    else:
        print(f"{algorithm_name} found no path.")

def draw_buttons(screen, buttons, button_width, button_height, screen_width, screen_height, button_color, button_font, button_font_color):
    spacing = (screen_width - (len(buttons) * button_width)) // (len(buttons) + 1)
    button_y = screen_height - button_height - 20  # 20 pixels margin from the bottom
    
    for i, button_text in enumerate(buttons):
        bx = spacing + i * (button_width + spacing)
        button_rect = pygame.Rect(bx, button_y, button_width, button_height)
        pygame.draw.rect(screen, button_color, button_rect)
        
        text_surface = button_font.render(button_text, True, button_font_color)
        text_rect = text_surface.get_rect(center=(bx + button_width // 2, button_y + button_height // 2))
        screen.blit(text_surface, text_rect)
    
    pygame.display.update()
    return spacing, button_y

def main():
    grid_data = create_grid(rows, cols)
    start = (0, 0)
    goal = (rows - 1, cols - 1)
    grid_data = add_obstacles(grid_data, int(rows * cols * 0.2), start, goal)

    draw_grid(screen, grid_data, cell_size)

    spacing, button_y = draw_buttons(screen, buttons, button_width, button_height, width, height, button_color, button_font, button_font_color)

    running = True
    selected_algorithm = None
    path = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, button_text in enumerate(buttons):
                    bx = spacing + i * (button_width + spacing)
                    if bx <= mouse_x <= bx + button_width and button_y <= mouse_y <= button_y + button_height:
                        selected_algorithm = button_text
                        path = None

        if selected_algorithm and not path:
            color = algorithm_colors[selected_algorithm]
            if selected_algorithm == "DFS":
                path = depth_first_search(grid_data, start, goal)
            elif selected_algorithm == "BFS":
                path = breadth_first_search(grid_data, start, goal)
            elif selected_algorithm == "A*":
                path = a_star_search(grid_data, start, goal)
            elif selected_algorithm == "Dijkstra":
                path = dijkstra_search(grid_data, start, goal)
            elif selected_algorithm == "UCS":
                path = uniform_cost_search(grid_data, start, goal)
            
            if path:
                visualize_path(screen, path, cell_size, color)
                display_path_info(selected_algorithm, path)
                selected_algorithm = None

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()