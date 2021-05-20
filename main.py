import pygame
import random

pygame.init()
running = True
white = (255, 255, 255)
WIDTH = 850
HEIGHT = 600
FONT = pygame.font.SysFont("Sans", 20)
TEXT_COLOR = (0, 0, 0)
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nome do Jogo')
bg = pygame.image.load("img/bg.png")

amarela = pygame.image.load('img/lxamarela.png')
azul = pygame.image.load('img/lxazul.png')
verde = pygame.image.load('img/lxverde.png')
vermelha = pygame.image.load('img/lxvermelha.png')

contador = 0
ponto = 0
objetos = ['Copos', 'Sacolas', 'Frascos', 'Potes', 'Tampinhas', 'Tubos de PVC',
           'Embalagens PET', 'Jornais', 'revistas', 'sulfite', 'rascunhos', 'folhas de caderno', 'formulários',
           'caixas de papelão', 'aparas de papel', 'envelopes', 'cartazes', 'panfletos', 'Tampinhas de garrafas',
           'lacres de latinhas', 'latas', 'ferragens', 'arames', 'chapas', 'canos', 'pregos', 'parafusos', 'porcas',
           'ferramentas', 'Garrafas', 'potes de conserva', 'Embalagens', 'Frascos', 'Vazios de remédios', 'Copos']

objetosProibidos = ['Cabos de panelas', 'Adesivos', 'Espuma', 'Acrílico', 'Embalagens metalizadas', 'Adesivos',
                    'papel carbono', 'Celofane', 'Guardanapos', 'bitucas de cigarro', 'papéis plastificados',
                    'metalizados', 'papéis sanitários', 'Clipes', 'grampos', 'esponjas de aço', 'aerossóis',
                    'latas de tinta', 'solventes ou químicos', 'latas de inseticida', 'Espelhos', 'Óculos',
                    'Boxes temperados', 'Pirex', 'Cerâmicas', 'Porcelanas', 'Tubos de TV', 'Tampas de forno']

vermelho_plastico = ['Copos', 'Sacolas', 'Frascos', 'Potes', 'Tampinhas', 'Tubos de PVC',
                     'Embalagens PET']

azul_papel = ['Jornais', 'revistas', 'sulfite', 'rascunhos', 'folhas de caderno', 'formulários', 'caixas de papelão',
              'aparas de papel', 'envelopes', 'cartazes', 'panfletos']
amarelo_metal = ['Tampinhas de garrafas', 'lacres de latinhas', 'latas', 'ferragens', 'arames', 'chapas', 'canos',
                 'pregos', 'parafusos', 'porcas', 'ferramentas']

verde_vidro = ['Garrafas', 'potes de conserva', 'Embalagens', 'Frascos', 'Vazios de remédios', 'Copos']

# Embaralha Lista de Objetos
random.shuffle(objetos)

while running:
    current_time = pygame.time.get_ticks()
    display_surface.blit(bg, (0, 0))
    pygame.time.set_timer(1, 2000)
    lixeiraVermelha = display_surface.blit(vermelha, (650, 391))
    lixeiraAmarela = display_surface.blit(amarela, (50, 385))
    lixeiraAzul = display_surface.blit(azul, (250, 390))
    lixeiraVerde = display_surface.blit(verde, (450, 396))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lixeiraAmarela.collidepoint(pygame.mouse.get_pos()):
                contador = contador + 1
                if objetos[contador] in amarelo_metal:
                    ponto = ponto + 1
                    display_surface.blit(pygame.image.load('img/correct.png'), (250, 180))
                else:
                    display_surface.blit(pygame.image.load('img/incorrect.png'), (250, 180))
            if lixeiraAzul.collidepoint(pygame.mouse.get_pos()):
                contador = contador + 1
                if objetos[contador] in azul_papel:
                    ponto = ponto + 1
                    display_surface.blit(pygame.image.load('img/correct.png'), (250, 180))
                else:
                    display_surface.blit(pygame.image.load('img/incorrect.png'), (250, 180))
            if lixeiraVerde.collidepoint(pygame.mouse.get_pos()):
                contador = contador + 1
                if objetos[contador] in verde_vidro:
                    ponto = ponto + 1
                    display_surface.blit(pygame.image.load('img/correct.png'), (250, 180))
                else:
                    display_surface.blit(pygame.image.load('img/incorrect.png'), (250, 180))
            if lixeiraVermelha.collidepoint(pygame.mouse.get_pos()):
                contador = contador + 1
                if objetos[contador] in vermelho_plastico:
                    ponto = ponto + 1
                    display_surface.blit(pygame.image.load('img/correct.png'), (250, 180))
                else:
                    display_surface.blit(pygame.image.load('img/incorrect.png'), (250, 180))
        if (contador == 10):
            running = False
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Display scores:
    font = pygame.font.Font(None, 40)
    text = font.render('Acertos: ' + str(ponto) + '/' + str(len(objetos)), True, (0, 0, 0))

    tempo = font.render(str(current_time), True, (0, 0, 0))

    display_surface.blit(text, (660, 10))
    display_surface.blit(tempo, (10, 10))

    objetoColeta = font.render(str(objetos[contador]).upper(), True, (0, 0, 0))
    display_surface.blit(objetoColeta, (370, 225))

    # Draws the surface object to the screen.
    pygame.display.update()
