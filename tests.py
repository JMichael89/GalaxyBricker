import pygame
import time

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Exemplo de Medição e Controle de FPS")

# Variáveis de controle do FPS
fps_alvo = 60  # FPS desejado
clock = pygame.time.Clock()

# Loop principal do jogo
running = True
while running:
    # Limitar a taxa de quadros por segundo
    clock.tick(fps_alvo)

    # Processamento de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica do jogo
    # ...

    # Renderização do jogo
    tela.fill((0, 0, 0))
    # ...

    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()