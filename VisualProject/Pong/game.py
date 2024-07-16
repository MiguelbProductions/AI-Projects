import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo da Barra')

# Cores
black = (0, 0, 0)
white = (255, 255, 255)

# Configurações da barra
bar_width = 10
bar_height = 100
bar_x = 50
bar_y = screen_height // 2 - bar_height // 2
bar_speed = 5

# Configurações da bola
ball_size = 20
ball_x = screen_width // 2 - ball_size // 2
ball_y = screen_height // 2 - ball_size // 2
ball_speed_x = 5
ball_speed_y = 5

# Função principal do jogo
def game_loop():
    global bar_y, ball_x, ball_y, ball_speed_x, ball_speed_y
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and bar_y > 0:
            bar_y -= bar_speed
        if keys[pygame.K_DOWN] and bar_y < screen_height - bar_height:
            bar_y += bar_speed

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_y <= 0 or ball_y >= screen_height - ball_size:
            ball_speed_y *= -1
        if ball_x <= 0:
            ball_x, ball_y = screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2
            ball_speed_x, ball_speed_y = random.choice([5, -5]), random.choice([5, -5])
        if ball_x >= screen_width - ball_size:
            ball_speed_x *= -1

        if bar_x < ball_x < bar_x + bar_width and bar_y < ball_y < bar_y + bar_height:
            ball_speed_x *= -1

        screen.fill(black)
        pygame.draw.rect(screen, white, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Iniciar o jogo
game_loop()
