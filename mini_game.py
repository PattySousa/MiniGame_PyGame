import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definição do tamanho da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Karate Doll Adventure')

# Definição das variáveis do personagem
doll_x = 50
doll_y = WINDOW_HEIGHT - 100
doll_width = 50
doll_height = 50
doll_speed = 5

# Classe para os obstáculos
class Obstacle:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def move(self):
        self.x -= self.speed

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

# Lista de obstáculos
obstacles = []

# Variável de pontuação
score = 0

# Loop principal do jogo
while True:
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles do personagem
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and doll_x > doll_speed:
        doll_x -= doll_speed
    if keys[pygame.K_RIGHT] and doll_x < WINDOW_WIDTH - doll_width - doll_speed:
        doll_x += doll_speed
    if keys[pygame.K_UP] and doll_y > doll_speed:
        doll_y -= doll_speed
    if keys[pygame.K_DOWN] and doll_y < WINDOW_HEIGHT - doll_height - doll_speed:
        doll_y += doll_speed

    # Adicionar obstáculos aleatoriamente
    if random.randint(0, 100) < 3:
        obstacle = Obstacle(WINDOW_WIDTH, random.randint(50, 500), 30, 30, BLACK, 5)
        obstacles.append(obstacle)

    # Mover e desenhar os obstáculos
    for obstacle in obstacles:
        obstacle.move()
        obstacle.draw(window)

        # Verificar colisão com o personagem
        if doll_x < obstacle.x + obstacle.width and doll_x + doll_width > obstacle.x and doll_y < obstacle.y + obstacle.height and doll_y + doll_height > obstacle.y:
            # Caso haja colisão, reinicie o jogo
            obstacles = []
            score = 0
            doll_x = 50
            doll_y = WINDOW_HEIGHT - 100

    # Verificar se o obstáculo saiu da tela
    if obstacle.x < 0:
        obstacles.remove(obstacle)
        score += 1

    # Mostrar a pontuação na tela
    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Score: {score}', True, BLACK)
    window.blit(text, (10, 10))

    # Desenho do personagem
    pygame.draw.rect(window, BLACK, (doll_x, doll_y, doll_width, doll_height))
    pygame.display.update()
