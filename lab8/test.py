import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set default drawing color
current_color = BLACK

# Set default drawing mode
current_mode = "pen"  # Can be "pen", "rectangle", "circle", or "eraser"

# Set default rectangle and circle parameters
start_pos = (0, 0)
end_pos = (0, 0)
radius = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_mode = "rectangle"
            elif event.key == pygame.K_c:
                current_mode = "circle"
            elif event.key == pygame.K_e:
                current_mode = "eraser"
            elif event.key == pygame.K_b:
                current_color = BLACK
            elif event.key == pygame.K_w:
                current_color = WHITE
            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()
            if current_mode == "rectangle":
                pygame.draw.rect(screen, current_color, (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
            elif current_mode == "circle":
                radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
                pygame.draw.circle(screen, current_color, (start_pos[0] + radius, start_pos[1] + radius), radius)
            elif current_mode == "eraser":
                pygame.draw.circle(screen, WHITE, end_pos, 20)  # Erase with a white circle
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
            if current_mode == "pen":
                pygame.draw.line(screen, current_color, event.pos, (event.pos[0] + 1, event.pos[1]))  # Draw line
    
    pygame.display.flip()

pygame.quit()
sys.exit()