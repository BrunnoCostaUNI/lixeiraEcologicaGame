import pygame
import random
import pygame_menu

pygame.init()
menuLigado = False
white = (255, 255, 255)
WIDTH = 850
HEIGHT = 600
FONT = pygame.font.SysFont("Sans", 20)
TEXT_COLOR = (0, 0, 0)
surface = pygame.display.set_mode((WIDTH, HEIGHT))
level = 10

menu = pygame_menu.Menu(HEIGHT, WIDTH, 'Lixeira Ecológica Game', theme=pygame_menu.themes.THEME_DARK)

def set_difficulty(value, difficulty):
    global level
    print(difficulty)
    if difficulty == 1:
        level = 10
    elif difficulty == 2:
        level = 20
    elif difficulty == 3:
        level = 30
    else:
        level = 0
    pass



def start_the_game():
    running = True
    display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Nome do Jogo')
    bg = pygame.image.load("img/bg.png")

    amarela = pygame.image.load('img/lxamarela.png')
    azul = pygame.image.load('img/lxazul.png')
    verde = pygame.image.load('img/lxverde.png')
    vermelha = pygame.image.load('img/lxvermelha.png')
    painel = pygame.image.load('img/painel.png')


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

    azul_papel = ['Jornais', 'revistas', 'sulfite', 'rascunhos', 'folhas de caderno', 'formulários',
                  'caixas de papelão',
                  'aparas de papel', 'envelopes', 'cartazes', 'panfletos']
    amarelo_metal = ['Tampinhas de garrafas', 'lacres de latinhas', 'latas', 'ferragens', 'arames', 'chapas', 'canos',
                     'pregos', 'parafusos', 'porcas', 'ferramentas']

    verde_vidro = ['Garrafas', 'potes de conserva', 'Embalagens', 'Frascos', 'Vazios de remédios', 'Copos']

    # Embaralha Lista de Objetos
    random.shuffle(objetos)

    while running:
        current_time = int(pygame.time.get_ticks() / 1000)
        display_surface.blit(bg, (0, 0))

        painel_imagem = display_surface.blit(painel, (0, 0))


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
                        display_surface.blit(pygame.image.load('img/correct.png'), (170, 180))
                    else:
                        display_surface.blit(pygame.image.load('img/incorrect.png'), (170, 180))
                if lixeiraAzul.collidepoint(pygame.mouse.get_pos()):
                    contador = contador + 1
                    if objetos[contador] in azul_papel:
                        ponto = ponto + 1
                        display_surface.blit(pygame.image.load('img/correct.png'), (170, 180))
                    else:
                        display_surface.blit(pygame.image.load('img/incorrect.png'), (170, 180))
                if lixeiraVerde.collidepoint(pygame.mouse.get_pos()):
                    contador = contador + 1
                    if objetos[contador] in verde_vidro:
                        ponto = ponto + 1
                        display_surface.blit(pygame.image.load('img/correct.png'), (170, 180))
                    else:
                        display_surface.blit(pygame.image.load('img/incorrect.png'), (170, 180))
                if lixeiraVermelha.collidepoint(pygame.mouse.get_pos()):
                    contador = contador + 1
                    if objetos[contador] in vermelho_plastico:
                        ponto = ponto + 1
                        display_surface.blit(pygame.image.load('img/correct.png'), (170, 180))
                    else:
                        display_surface.blit(pygame.image.load('img/incorrect.png'), (170, 180))
            if contador == level:
                running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Display scores:
        font = pygame.font.Font(None, 40)
        text = font.render(str(ponto) + '/' + str(level), True, (0, 0, 0))
        jogadas = font.render(str(contador) + ' de ' + str(level), True, (0, 0, 0))
        tempo = font.render(str(current_time), True, (0, 0, 0))

        display_surface.blit(text, (750, 10))
        display_surface.blit(jogadas, (420, 10))
        display_surface.blit(tempo, (130, 8))

        objetoColeta = font.render(str(objetos[contador]).upper(), True, (36, 36, 36))

        display_surface.blit(objetoColeta, (330, 225))

        # Draws the surface object to the screen.
        pygame.display.update()

    pass


menu.add.text_input('Nome: ', default='John Doe')
menu.add.selector('Dificuldade: ', [(' Fácil  ', 1), ('Médio', 2), ('Difícil ', 3)], onchange=set_difficulty)
menu.add.button('Jogar', start_the_game)
menu.add.button('Sair', pygame_menu.events.EXIT)

menu.mainloop(surface)