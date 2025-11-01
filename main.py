import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (34, 34, 34)  # Dark gray
FPS = 60

# Colors
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
DARK_GOLD = (184, 134, 11)
BUTTON_HOVER = (255, 235, 50)
SHADOW_COLOR = (10, 10, 15)

# Game states
TITLE_SCREEN = "title"
GAME_PLAYING = "playing"

# Display window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Shadows of the Golden Door")

# Clock for controlling frame rate and delta time
clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.Font(None, 72)
subtitle_font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 48)
instruction_font = pygame.font.Font(None, 24)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.hovered = False
    
    def draw(self, surface):
        # Draw shadow
        shadow_rect = self.rect.copy()
        shadow_rect.x += 4
        shadow_rect.y += 4
        pygame.draw.rect(surface, SHADOW_COLOR, shadow_rect, border_radius=10)
        
        # Draw button
        color = BUTTON_HOVER if self.hovered else GOLD
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, DARK_GOLD, self.rect, 3, border_radius=10)
        
        # Draw text
        text_surface = self.font.render(self.text, True, BACKGROUND_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def check_hover(self, pos):
        self.hovered = self.rect.collidepoint(pos)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Player properties
player_width = 50
player_height = 50
player_color = (255, 255, 0)  # Yellow
player_speed = 300  # Pixels per second

# Player initial position using a Vector2 for float precision
# Center the player initially
player_pos = pygame.math.Vector2(
    WINDOW_WIDTH / 2 - player_width / 2,
    WINDOW_HEIGHT / 2 - player_height / 2
)

# Initialize game objects
start_button = Button(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 50, 200, 60, "START", button_font)
game_state = TITLE_SCREEN

def draw_title_screen():
    """Draw the title screen"""
    screen.fill(BACKGROUND_COLOR)
    
    # Draw title with shadow effect
    title_text = "Shadows of the"
    title_surface = title_font.render(title_text, True, SHADOW_COLOR)
    title_rect = title_surface.get_rect(center=(WINDOW_WIDTH // 2 + 2, 150 + 2))
    screen.blit(title_surface, title_rect)
    
    title_surface = title_font.render(title_text, True, WHITE)
    title_rect = title_surface.get_rect(center=(WINDOW_WIDTH // 2, 150))
    screen.blit(title_surface, title_rect)
    
    # Draw "Golden Door" in gold
    golden_text = "Golden Door"
    golden_surface = title_font.render(golden_text, True, SHADOW_COLOR)
    golden_rect = golden_surface.get_rect(center=(WINDOW_WIDTH // 2 + 2, 220 + 2))
    screen.blit(golden_surface, golden_rect)
    
    golden_surface = title_font.render(golden_text, True, GOLD)
    golden_rect = golden_surface.get_rect(center=(WINDOW_WIDTH // 2, 220))
    screen.blit(golden_surface, golden_rect)
    
    # Draw subtitle
    subtitle_text = "Find the three lost keys to escape"
    subtitle_surface = subtitle_font.render(subtitle_text, True, WHITE)
    subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_WIDTH // 2, 300))
    screen.blit(subtitle_surface, subtitle_rect)
    
    # Draw decorative key symbols
    for i in range(3):
        key_x = WINDOW_WIDTH // 2 - 60 + i * 60
        pygame.draw.rect(screen, GOLD, (key_x, 340, 30, 30), border_radius=3)
        pygame.draw.circle(screen, BACKGROUND_COLOR, (key_x + 15, 355), 8)
    
    # Draw start button
    start_button.draw(screen)
    
    # Draw instructions at bottom
    instruction_text = "Use WASD or Arrow Keys to move"
    instruction_surface = instruction_font.render(instruction_text, True, WHITE)
    instruction_rect = instruction_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 40))
    screen.blit(instruction_surface, instruction_rect)

def draw_game_screen():
    """Draw the main game screen"""
    screen.fill(BACKGROUND_COLOR)
    
    # Draw a simple maze border
    pygame.draw.rect(screen, GOLD, (50, 50, WINDOW_WIDTH - 100, WINDOW_HEIGHT - 100), 3)
    
    # Create a Rect from the float-based player_pos for rendering
    # Using round() is slightly more accurate than int() truncation
    player_rect = pygame.Rect(round(player_pos.x), round(player_pos.y), player_width, player_height)
    pygame.draw.rect(screen, player_color, player_rect)
    
    # Draw game title at top
    game_title = subtitle_font.render("Ancient Labyrinth", True, GOLD)
    game_title_rect = game_title.get_rect(center=(WINDOW_WIDTH // 2, 30))
    screen.blit(game_title, game_title_rect)
    
    # Draw instructions
    instruction_text = "Move with WASD or Arrow Keys | ESC to return to title"
    instruction_surface = instruction_font.render(instruction_text, True, WHITE)
    instruction_rect = instruction_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 20))
    screen.blit(instruction_surface, instruction_rect)

# Game loop
running = True
while running:
    # clock.tick returns milliseconds since last frame. Divide by 1000 for seconds.
    # dt (delta time) makes movement frame-rate independent.
    dt = clock.tick(FPS) / 1000.0
    
    mouse_pos = pygame.mouse.get_pos()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == TITLE_SCREEN and start_button.is_clicked(mouse_pos):
                game_state = GAME_PLAYING
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and game_state == GAME_PLAYING:
                game_state = TITLE_SCREEN
    
    # Update
    if game_state == TITLE_SCREEN:
        start_button.check_hover(mouse_pos)
    elif game_state == GAME_PLAYING:
        # Get state of all keys currently pressed
        keys = pygame.key.get_pressed()
        
        # Calculate movement direction vector
        # Using boolean arithmetic (True=1, False=0) for a concise way to get -1, 0, or 1
        direction = pygame.math.Vector2(
            (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a]),
            (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])
        )
        
        # Normalize the direction vector to ensure consistent speed, if there is movement
        if direction.length_squared() > 0:  # Use length_squared() to avoid a square root calculation
            direction.normalize_ip()
        
        # Update player position based on speed, direction, and delta time
        player_pos += direction * player_speed * dt
        
        # Implement boundary detection (clamping)
        player_pos.x = max(0, min(player_pos.x, WINDOW_WIDTH - player_width))
        player_pos.y = max(0, min(player_pos.y, WINDOW_HEIGHT - player_height))
    
    # Rendering
    if game_state == TITLE_SCREEN:
        draw_title_screen()
    elif game_state == GAME_PLAYING:
        draw_game_screen()
    
    # Update the display
    pygame.display.flip()

# Quit Pygame and exit the program
pygame.quit()
sys.exit()