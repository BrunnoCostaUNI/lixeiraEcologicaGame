import pygame
import random
import pygame_menu



pygame.init()

#VARIÁVEIS GLOBAIS
menuLigado = False
white = (255, 255, 255)
WIDTH = 850
HEIGHT = 600
FONT = pygame.font.SysFont("comicsansms", 50)
TEXT_COLOR = (0, 0, 0)
surface = pygame.display.set_mode((WIDTH, HEIGHT))
level = 10
poluicao = 0
levelPoluicao = 10
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))


BACK = 'img/bg.png'
menu = pygame_menu.Menu(HEIGHT, WIDTH, 'Lixeira Ecológica Game', theme=pygame_menu.themes.THEME_DARK)

#FUNÇÃO PARA TRATAR DIFICULDADE
def set_difficulty(value, difficulty):
    global level
    global levelPoluicao
    print(difficulty)
    if difficulty == 1:
        level = 10
        levelPoluicao = 10
    elif difficulty == 2:
        level = 20
        levelPoluicao = 5
    elif difficulty == 3:
        level = 30
        levelPoluicao = 3.333
    else:
        level = 0
    pass

#INSTRUÇÃO COLETA
def start_manual():
    manual_running = True
    bg = pygame.image.load("img/bg.png").convert(24)
    display_surface.blit(bg, (0, 0))



    while manual_running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 109:
                    manual_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                manual_running =False


        # Display scores:
        font = pygame.font.Font(None, 40)

        titulo_cores = font.render('Código de Cores - Coleta Seletiva', True, (0, 0, 0))
        text_azul = font.render('Azul: papel/papelão', True, (0, 0, 0))
        text_vermelho = font.render('Vermelho: plástico', True, (0, 0, 0))
        text_verde = font.render('Verde: vidro', True, (0, 0, 0))
        text_amarelo = font.render('Amarelo: metal', True, (0, 0, 0))
        voltar_menu = font.render('Aperte [m] ou clique com o mouse para voltar ao menu.', True, (0, 0, 0))


        display_surface.blit(titulo_cores, (200, 10))
        display_surface.blit(text_azul, (300, 100))
        display_surface.blit(text_vermelho, (300,170))
        display_surface.blit(text_verde, (300, 240))
        display_surface.blit(text_amarelo, (300, 310))
        display_surface.blit(voltar_menu, (40, 500))


        # Draws the surface object to the screen.
        pygame.display.update()

    pass


#FUNÇÃO PARA INICIAR JOGO
def start_the_game():
    running = True
    placar_show = False

    pygame.display.set_caption('Lixeira Ecológica Game')
    bg = pygame.image.load("img/bg.png").convert(24)
    bg.set_alpha(50)

    amarela = pygame.image.load('img/lxamarela.png')
    azul = pygame.image.load('img/lxazul.png')
    verde = pygame.image.load('img/lxverde.png')
    vermelha = pygame.image.load('img/lxvermelha.png')
    painel = pygame.image.load('img/painel.png')



    contador = 0
    ponto = 0
    objetos = ['Copos', 'Sacolas', 'Frascos', 'Potes', 'Tampinhas', 'Tubos de PVC',
               'Embalagens PET', 'Jornais', 'revistas', 'sulfite', 'rascunhos', 'folhas de caderno', 'formularios',
               'caixas de papelao', 'aparas de papel', 'envelopes', 'cartazes', 'panfletos', 'Tampinhas de garrafas',
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
                  'caixas de papelao',
                  'aparas de papel', 'envelopes', 'cartazes', 'panfletos']
    amarelo_metal = ['Tampinhas de garrafas', 'lacres de latinhas', 'latas', 'ferragens', 'arames', 'chapas', 'canos',
                     'pregos', 'parafusos', 'porcas', 'ferramentas']

    verde_vidro = ['Garrafas', 'potes de conserva', 'Embalagens', 'Frascos', 'Vazios de remédios', 'Copos']

    # Embaralha Lista de Objetos
    random.shuffle(objetos)

    taCerto = True

    while running:

        current_time = int(pygame.time.get_ticks() / 1000)
        display_surface.blit(bg, (0, 0))

        painel_imagem = display_surface.blit(painel, (0, 0))

        lixeiraVermelha = display_surface.blit(vermelha, (650, 391))
        lixeiraAmarela = display_surface.blit(amarela, (50, 385))
        lixeiraAzul = display_surface.blit(azul, (250, 390))
        lixeiraVerde = display_surface.blit(verde, (450, 396))

        global poluicao



        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 109:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if placar_show == True:
                    print('Partida Finalizada')
                else:
                    if lixeiraAmarela.collidepoint(pygame.mouse.get_pos()):
                        if objetos[contador] in amarelo_metal:
                            display_surface.blit(pygame.image.load('img/correct.png'), (200, 180))
                            ponto = ponto + 1
                        else:
                            display_surface.blit(pygame.image.load('img/incorrect.png'), (200, 180))
                            poluicao = poluicao + levelPoluicao
                        contador = contador + 1
                    if lixeiraAzul.collidepoint(pygame.mouse.get_pos()):

                        if objetos[contador] in azul_papel:
                            display_surface.blit(pygame.image.load('img/correct.png'), (200, 180))
                            ponto = ponto + 1
                        else:
                            display_surface.blit(pygame.image.load('img/incorrect.png'), (200, 180))
                            poluicao = poluicao + levelPoluicao
                        contador = contador + 1
                    if lixeiraVerde.collidepoint(pygame.mouse.get_pos()):

                        if objetos[contador] in verde_vidro:
                            display_surface.blit(pygame.image.load('img/correct.png'), (200, 180))
                            ponto = ponto + 1
                        else:
                            display_surface.blit(pygame.image.load('img/incorrect.png'), (200, 180))
                            poluicao = poluicao + levelPoluicao
                        contador = contador + 1
                    if lixeiraVermelha.collidepoint(pygame.mouse.get_pos()):

                        if objetos[contador] in vermelho_plastico:
                            display_surface.blit(pygame.image.load('img/correct.png'), (200, 180))
                            ponto = ponto + 1
                        else:
                            display_surface.blit(pygame.image.load('img/incorrect.png'), (200, 180))
                            poluicao = poluicao + levelPoluicao
                        contador = contador + 1
            if contador == level:
                placar_show = True
                #running = False
                poluicao = 0
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

        objetoColeta = font.render(str(objetos[contador]).upper(), 'True', (36, 36, 36))

        display_surface.blit(objetoColeta, (320, 225))
        pygame.gfxdraw.box(surface, pygame.Rect(0, 43, WIDTH, 557), (0, 0, 0, poluicao))

        if placar_show == True:
            placar = pygame.image.load('img/placar_ge.png')
            painel_position = display_surface.blit(placar, (0, 0))
            font_placar = pygame.font.Font(None, 60)
            font_reset = pygame.font.Font(None, 30)
            pontuacao = font_placar.render(str(ponto) + ' de ' + str(level), True, (255, 255, 255))
            display_surface.blit(pontuacao, (345, 285))


        # Draws the surface object to the screen.
        pygame.display.update()

    pass





#MENU PRINCIPAL
menu.add.text_input('Nome: ', default='John Doe')
menu.add.selector('Dificuldade: ', [(' Fácil  ', 1), ('Médio', 2), ('Difícil ', 3)], onchange=set_difficulty)
menu.add.button('Manual', start_manual)
menu.add.button('Jogar', start_the_game)
menu.add.button('Sair', pygame_menu.events.EXIT)

menu.mainloop(surface)
