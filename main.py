import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (34, 34, 34) # Dark gray
FPS = 60

# Display window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Shadows of the Golden Door")

# Clock for controlling frame rate and delta time
clock = pygame.time.Clock()

# Player properties
player_width = 50
player_height = 50
player_color = (255, 255, 0) # Yellow
player_speed = 300 # Pixels per second

# Player initial position using a Vector2 for float precision
# Center the player initially
player_pos = pygame.math.Vector2(
    WINDOW_WIDTH / 2 - player_width / 2,
    WINDOW_HEIGHT / 2 - player_height / 2
)

# Game loop
running = True
while running:
    # clock.tick returns milliseconds since last frame. Divide by 1000 for seconds.
    # dt (delta time) makes movement frame-rate independent.
    dt = clock.tick(FPS) / 1000.0

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get state of all keys currently pressed
    keys = pygame.key.get_pressed()

    # Calculate movement direction vector
    # Using boolean arithmetic (True=1, False=0) for a concise way to get -1, 0, or 1
    direction = pygame.math.Vector2(
        (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a]),
        (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])
    )

    # Normalize the direction vector to ensure consistent speed, if there is movement
    if direction.length_squared() > 0: # Use length_squared() to avoid a square root calculation
        direction.normalize_ip()

    # Update player position based on speed, direction, and delta time
    player_pos += direction * player_speed * dt

    # Implement boundary detection (clamping)
    player_pos.x = max(0, min(player_pos.x, WINDOW_WIDTH - player_width))
    player_pos.y = max(0, min(player_pos.y, WINDOW_HEIGHT - player_height))

    # Create a Rect from the float-based player_pos for rendering
    # Using round() is slightly more accurate than int() truncation
    player_rect = pygame.Rect(round(player_pos.x), round(player_pos.y), player_width, player_height)

    # Rendering
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, player_color, player_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame and exit the program
pygame.quit()
sys.exit()