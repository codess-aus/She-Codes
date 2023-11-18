import pygame
import random

# Game Setup
SCREEN_WIDTH, SCREEN_HEIGHT = 650, 650
PLAYER_COLOR = (255, 140, 0)  # darkorange
FOOD_COLOR = (144, 238, 144)  # lightgreen
BG_COLOR = (0, 0, 0)  # black
PLAYER_SIZE = 20
FOOD_SIZE = 10
MAX_FOODS = 10

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Player Setup
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

# Food Setup
foods = []
for _ in range(MAX_FOODS):
    x = random.randint(0, SCREEN_WIDTH - FOOD_SIZE)
    y = random.randint(0, SCREEN_HEIGHT - FOOD_SIZE)
    foods.append([x, y])

# Game Loop
running = True
score = 0
while running:
    clock.tick(30)  # Cap at 30 FPS
    screen.fill(BG_COLOR)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Draw Player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    # Draw Foods
    for food in foods:
        pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], FOOD_SIZE, FOOD_SIZE))

    # Check for collisions
    player_rect = pygame.Rect(player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE)
    for food in foods:
        food_rect = pygame.Rect(food[0], food[1], FOOD_SIZE, FOOD_SIZE)
        if player_rect.colliderect(food_rect):
            score += 1
            foods.remove(food)
            x = random.randint(0, SCREEN_WIDTH - FOOD_SIZE)
            y = random.randint(0, SCREEN_HEIGHT - FOOD_SIZE)
            foods.append([x, y])

    # Display Score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
