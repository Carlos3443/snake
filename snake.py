import pygame
from random import randrange

''' Building the snake background'''
pygame.init()
WINDOW = 800
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

'''Set up how the snake will appear inside the interface'''
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pygame.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE -2])
snake.center = get_random_position()
length = 1
alive = True
pygame.display.set_caption("Snake")

'''Variable for how the snake will grow'''
segments = [snake.copy()]

snake_dir = (0, 0)
time, time_step = 0, 110

'''Variables for food tokens for the snake to get'''
food = snake.copy()

food.center = get_random_position()
screen = pygame.display.set_mode([WINDOW] * 2)
clock = pygame.time.Clock()
dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}

while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False

        '''Logic for key presses for the snake to move'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and dirs[pygame.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
            if event.key == pygame.K_s and dirs[pygame.K_s]:
                snake_dir = (0, TILE_SIZE)
                dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
            if event.key == pygame.K_a and dirs[pygame.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
            if event.key == pygame.K_d and dirs[pygame.K_d]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
    screen.fill('black')

    '''Logic for score keeping'''
    font = pygame.font.SysFont('arial', 30)
    score = font.render(f'Score: {length}', True, (255, 255, 255))
    screen.blit(score, (600, 10))

    '''Code for game to detect if snake collides with itself'''
    self_eating = pygame.Rect.collidelist(snake, segments[:-1]) != -1

    '''Code for determining when snake should restart'''
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

    '''Food creation code'''
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
        score = font.render(f'Score: {length}', True, (255, 255, 255))
        screen.blit(score, (600, 10))
    pygame.draw.rect(screen, 'red', food)
    [pygame.draw.rect(screen, 'green', segment) for segment in segments]
    time_now = pygame.time.get_ticks()

    '''Code for setting up the pace of the game'''
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    pygame.display.flip()
    clock.tick(60)