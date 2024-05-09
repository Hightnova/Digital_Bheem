import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up screen
width = 600
height = 400
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake attributes
snake_speed = 10
snake_position = [width // 2, height // 2]
snake_body = [[width // 2, height // 2]]
direction = 'RIGHT'
change_to = direction

# Food attributes
food_position = [random.randrange(1, (width // cell_size)) * cell_size,
                 random.randrange(1, (height // cell_size)) * cell_size]
food_spawn = True

# Score
score = 0

# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    screen.fill(WHITE)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.quit()
    sys.exit()

# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update direction
    direction = change_to

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= cell_size
    if direction == 'DOWN':
        snake_position[1] += cell_size
    if direction == 'LEFT':
        snake_position[0] -= cell_size
    if direction == 'RIGHT':
        snake_position[0] += cell_size

    # Snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food
    if not food_spawn:
        food_position = [random.randrange(1, (width // cell_size)) * cell_size,
                         random.randrange(1, (height // cell_size)) * cell_size]
    food_spawn = True

    # Draw on screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, pygame.Rect(food_position[0], food_position[1], cell_size, cell_size))

    for pos in snake_body:
        pygame.draw.rect(screen, BLACK, pygame.Rect(pos[0], pos[1], cell_size, cell_size))

    # Game Over conditions
    if (snake_position[0] < 0 or snake_position[0] > width - cell_size or
            snake_position[1] < 0 or snake_position[1] > height - cell_size):
        game_over()

    # Collision with itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Score display
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render('Score : ' + str(score), True, BLACK)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width / 10, 15)
    screen.blit(score_surface, score_rect)
    pygame.display.update()

    # Refresh rate
    pygame.time.Clock().tick(snake_speed)
