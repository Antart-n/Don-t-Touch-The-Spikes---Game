#IMPORTAÇÕES:
import pygame
from random import choice
from funcionalidades import elementos, imagens, mecanicas, arquivos

#INICIAR PYGAME:
pygame.init()

#SPRITES DO JOGO:
sprites = {
    'passaro': [pygame.image.load(f'Sprites/passaro {num}.png') for num in range(1, 4)],
    'logotipo': pygame.image.load('Sprites/Banner.png'),
    'replay': pygame.image.load('Menu/replay.png'),
    'pontos': pygame.image.load('Menu/pontos.png')
}
elementos.redimensionar_lista_elementos(sprites['passaro'], (50, 50))
sprites['pontos'] = pygame.transform.scale(sprites['pontos'], (sprites['pontos'].get_width() / 3, sprites['pontos'].get_height() / 3))
sprites['replay'] = pygame.transform.scale(sprites['replay'], (sprites['replay'].get_width() / 3, sprites['replay'].get_height() / 3))

#SONS DO JOGO:
sons = {
    'pulo': pygame.mixer.Sound('Som/som pulo.mp3'),
    'colisão': pygame.mixer.Sound('Som/som colisão.mp3'),
    'morte': pygame.mixer.Sound('Som/som morte.mp3')
}

#JANELA E COMPONENTES:
#Dimensões da janela
dimensões = [1000, 800]
#Definir Janela
janela = pygame.display.set_mode(dimensões)
#Titulo da janela
pygame.display.set_caption("Don't Touch The Spikes")
#Cor base da janela:
cor_base = [65, 65, 65]
#Icone da Janela
pygame.display.set_icon(sprites['logotipo'])

#FONTE E TEXTO:
#Fontes utilizadas:
fontes = (pygame.font.Font("Fontes/HackerNoonV2-Regular.ttf", 100), pygame.font.Font("Fontes/Montserrat-Medium.ttf", 40))
#Textos exibidos:
texto = {
    'Iniciar': fontes[1].render('TAP TO JUMP', True, (255, 51, 100))
}

#ELEMENTOS DE FUNDO E MENU:
#Lista de elementos
lista_elementos = [elementos.Elementos(janela, 'rect', (200, 200, 200), ((dimensões[0] - 405) / 2, (dimensões[1] - 600) / 2, 405, 600)),
                   elementos.Elementos(janela, 'circle', (255, 255, 255), (dimensões[0] / 2, dimensões[1] / 2), 125, 0),
                   imagens.Imagens(janela, sprites['replay'], [(dimensões[0] / 2) - (sprites['replay'].get_width() / 2), (dimensões[1] / 2) + (sprites['pontos'].get_height() / 2)]),
                   imagens.Imagens(janela, sprites['pontos'], [(dimensões[0] / 2) - (sprites['pontos'].get_width() / 2), (dimensões[1] / 2) - (sprites['pontos'].get_height() / 2)])]
lista_elementos[2].Definir_rect()

#DEFININDO ESPINHOS:
#Definindo todas as posição dos espinhos:
posiçoes_espinhos = {
    'direita': mecanicas.criarListaPosiçoes(
        [(lista_elementos[0].posição[0] + lista_elementos[0].posição[2] - 25), lista_elementos[0].posição[1]], 10, 50, 1),
    'esquerda': mecanicas.criarListaPosiçoes(
        [lista_elementos[0].posição[0], lista_elementos[0].posição[1]], 10, 50, 1),
    'cima': mecanicas.criarListaPosiçoes(
        [lista_elementos[0].posição[0], lista_elementos[0].posição[1]], 6, 50, 0),
    'baixo': mecanicas.criarListaPosiçoes(
        [lista_elementos[0].posição[0], (lista_elementos[0].posição[1] + lista_elementos[0].posição[-1] - 25)], 6, 50, 0)
}
#Cria duas superficie base (Horizontal e Vertical) para inserir os espinhos:
superficie_obstaculos = (pygame.Surface((50, 25), pygame.SRCALPHA), pygame.Surface((25, 50), pygame.SRCALPHA))
#Defini os epinhos em copias das superficie base:
espinhos_em_superficie = {
    'direita': elementos.Elementos(superficie_obstaculos[1].copy(), 'polygon', (cor_base + [255]), ((25, 0), (25, 50), (0, 25))),
    'esquerda': elementos.Elementos(superficie_obstaculos[1].copy(), 'polygon', (cor_base + [255]), ((0, 0), (0, 50), (25, 25))),
    'cima': elementos.Elementos(superficie_obstaculos[0].copy(), 'polygon', (cor_base + [255]), ((0, 0), (50, 0), (25, 25))),
    'baixo': elementos.Elementos(superficie_obstaculos[0].copy(), 'polygon', (cor_base + [255]), ((0, 25), (50, 25), (25, 0)))
}
#Exibi os espinhos nas superficies:
elementos.MostrarConjuntoElementos(espinhos_em_superficie)
#Cria uma lista com todas as combinações dos espinhos laterais:
combinações_de_obstaculos = [
    [1, 7], [3, 7, 8], [0, 4, 5, 9], [1, 2, 4, 7, 9], [0, 2, 4, 6, 8, 9], [0, 2, 4, 5, 6, 8, 9],
    [4, 7], [1, 3, 7], [0, 3, 4, 6], [1, 4, 6, 7, 9], [2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 6, 8, 9],
    [0, 5], [0, 5, 7], [1, 3, 4, 6], [3, 4, 5, 6, 9], [0, 1, 4, 5, 6, 8], [1, 2, 3, 5, 6, 8, 9],
    [6, 7], [0, 2, 7], [3, 4, 7, 9], [2, 3, 4, 6, 9], [0, 2, 4, 5, 6, 7], [0, 1, 5, 6, 7, 8, 9],
    [5, 6], [4, 6, 9], [0, 3, 8, 9], [0, 3, 4, 5, 7], [0, 3, 5, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7],
    [2, 3], [0, 8, 9], [0, 2, 3, 7], [1, 2, 4, 7, 9], [1, 2, 3, 6, 7, 9], [2, 4, 5, 6, 7, 8, 9],
    [2, 5], [0, 3, 7], [4, 5, 6, 8], [1, 2, 3, 6, 9], [1, 3, 4, 6, 8, 9], [0, 1, 2, 4, 6, 8, 9]
]

#DEFINE PARA NÃO ABRIR O MENU DE REINICIAR:
menu = False

#DEFINE A VARIAVEL DE PONTUAÇÃO:
pontuação = 0

#DEFINE A VARIAVEL QUE CONTROLA A DIREÇÃO DO PASSARO:
direção_passaro = 0

#LOOP GLOBAL:
while True:
    #Variavel de controle do jogo:
    rodar_jogo = False
    #Cria a varivel que determina o lado onde aparecerão os espinhos:
    lado_obstaculos = True
    #Lista de espinhos que estão na tela:
    lista_de_obstaculos = {
        'espinhos cima': [imagens.Imagens(janela, espinhos_em_superficie['cima'].superficie, posiçao) for posiçao in posiçoes_espinhos['cima']],
        'espinhos baixo': [imagens.Imagens(janela, espinhos_em_superficie['baixo'].superficie, posiçao) for posiçao in posiçoes_espinhos['baixo']],
        'espinhos': list()
    }
    #Limite de RPS do loop do jogo (Reptições por segundo):
    rps = 60
    #Relogio - Timer de RPS
    relogio = pygame.time.Clock()
    #Define a variavel que faz o trabalho da gravidade, diminuindo a cada iteração a resistencia do pulo:
    diminuição = 0.50

    #VERIFICA OS EVENTOS NO MENU INCIAL E MENU DE MORTE:
    for evento in pygame.event.get():
        #Fecha o jogo caso X no canto superior direito seja pressionado:
        if evento.type == pygame.QUIT:
            exit()

        #Verifica se houve alguma tecla foi pressionada no mouse e no teclado:
        elif evento.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYUP):
            #Tenta verificar se o botão direito no mouse foi pressionado:
            try:
                if evento.button == 1:
                    #Verifica se o menu de morte esta aberto:
                    if menu:
                        clique = pygame.Rect(evento.pos[0], evento.pos[1], 1, 1)
                        replay = clique.colliderect(lista_elementos[2].posição)
                        #Caso o botão de "replay", seja pressionado o menu de morte será fechado:
                        if replay:
                            menu = False
                    #Caso o menu inicial esteja aberto o jogo ira começar:
                    else:
                        rodar_jogo = True

            #Caso as ações no mouse deem errado, verifica se as teclas (espaço, botão_cima, w) foram pressionados:
            except:
                if evento.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                    #Caso o menu de morte esteja aberto, ele o fechará:
                    if menu:
                        menu = False
                    #Caso o menu inicial esteja aberto o jogo ira começar:
                    else:
                        rodar_jogo = True


    janela.fill(cor_base)
    elementos.MostrarConjuntoElementos(lista_elementos[:2])

    #MENU DE MORTE:
    if menu:

        #PONTUAÇÃO:
        #Define o texto para exibir a pontuação feita:
        pontuação_texto = fontes[1].render(f'{pontuação}', True, (255, 255, 255))
        #Define a posição do texto da pontuação:
        pos_pontuação = ((dimensões[0] / 2) - (pontuação_texto.get_width() / 2), (dimensões[1] / 2) - (pontuação_texto.get_height() / 2 + 15))
        #Exibi o botão de "replay" e painel de pontuação:
        imagens.MostrarConjuntoImagens(lista_elementos[2:])
        #Exibi a pontuação feita no painel de pontuação:
        janela.blit(pontuação_texto, pos_pontuação)

        #RECORDE:
        #Verifica se há um arquivo "recorde", caso contrário um novo será criado:
        arquivos.verificar_arquivo('recorde', '0')
        #Abre o o arquivo de recordes:
        recorde = open('recorde', 'r+')
        #Verifica se pontuação é superior ao recorde:
        if pontuação > int(recorde.read()):
            #Substitui o recorde anterior pelo novo recorde:
            recorde.seek(0)
            recorde.write(str(pontuação))
        recorde.seek(0)
        #Cria um novo parametros na biblioteca de textos para o recorde:
        texto['recorde txt'] = fontes[1].render(f'BEST SCORE {recorde.read()}', True, cor_base)
        #Fecha o arquivo "recorde":
        recorde.close()
        #Exibi o recorde na tela:
        janela.blit(texto['recorde txt'], ((dimensões[0] / 2) - (texto['recorde txt'].get_width() / 2), (dimensões[1] / 1.4)))
        
        #SPRITE DE MORTE DO PASSARO:
        #Altera o sprite do passaro:
        passaro.imagem = sprites['passaro'][2]
    
    #MENU INICIAL:
    else:

        #RENICIAR COMPONENTES PRINCIPAIS:
        #reinicia a a cor base do jogo:
        cor_base = [65, 65, 65]
        #reinicia a cor do fundo do jogo:
        lista_elementos[0].cor = [200, 200, 200]
        #Ajusta para qual direção o pasaro está virado:
        if pontuação % 2 != 0:
            imagens.espelhamento_conjunto_imagens(sprites['passaro'], 1, 0)
        #reinicia a pontuação:
        pontuação = 0

        #Mostra o texto de "TAP TO JUMP" na tela:
        janela.blit(texto['Iniciar'], ((dimensões[0] / 2) - (texto['Iniciar'].get_width() / 2), (dimensões[1] / 4)))

        #PASSARO:
        #Define a posição do passaro no menu inicial:
        posição_passaro = [(dimensões[0] / 2) - (50 / 2), (dimensões[1] / 2) - (50 / 2)]
        #Define o sprite do passaro no menu inicial:
        passaro = imagens.Imagens(janela, sprites['passaro'][0], posição_passaro, [5, -10])
    
    #Exibi o passaro na tela:
    passaro.mostrarImagem()
    
    #ESPINHOS:
    #Exibi todos os espinhos em tela:
    imagens.MostrarConjuntoImagens(lista_de_obstaculos)

    #Reinicia a cor de todos os espinhos:
    elementos.alterar_cor_conjunto_elementos(espinhos_em_superficie, cor_base)
    #Atribui a os espinhos com sua cor reiniciada a suas superficies:
    elementos.MostrarConjuntoElementos(espinhos_em_superficie)

    #ATUALIZA A JANELA:
    pygame.display.update()

    #LOOP DO JOGO:
    while rodar_jogo:
        #Altera para abrir o menu de morte ao morrer:
        menu = True
        #Limpar a janela
        janela.fill(cor_base)
        #Tratar eventos
        for eventos in pygame.event.get():
        #Fecha o jogo caso X no canto superior direito seja pressionado:
            if eventos.type == pygame.QUIT:
                rodar_jogo = False

            #Verifica se algum botão no mouse foi pressionado:
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                #Verifca se o botão direito do mouse foi pressionado:
                if eventos.button == 1:
                    #Toca o som de pulo:
                    pygame.mixer.Sound.play(sons['pulo'])
                    #Altera as configurações de pulo para o passaro subir:
                    passaro.desloc[1] = -10
                    diminuição = 0.50

            #Verifica se algum botão no teclado foi pressionado:
            elif eventos.type == pygame.KEYDOWN:
                #Verifica se as teclas (espaço, botão_cima, w) foram pressionadas:
                if eventos.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                    #Toca o som de pulo:
                    pygame.mixer.Sound.play(sons['pulo'])
                    #Altera as configurações de pulo para o passaro subir:
                    passaro.desloc[1] = -10
                    diminuição = 0.50

        #COLISÃO COM PAREDES:
        #Verifica se o passaro colidiu com alguma parede lateral:
        if passaro.posição[0] >= sum(lista_elementos[0].posição[:3:2]) - 50 or passaro.posição[0] <= lista_elementos[0].posição[0]:
            #Toca o som de pontuação:
            pygame.mixer.Sound.play(sons['colisão'])
            #Aumenta a pontuação em 1 ponto:
            pontuação += 1
            #Altera a direção do passaro:
            if direção_passaro == 0:
                direção_passaro = 1
            imagens.espelhamento_conjunto_imagens(sprites['passaro'], direção_passaro, 0)

            #ALTERA A COR E COMBINAÇÃO DE ESPINHOS DO JOGO COM BASE NA PONTUAÇÃO:
            #Dentro de uma margem de 0 a 4, serão combinações de 2 espinhos:
            if pontuação <= 4:
                combinação = choice(combinações_de_obstaculos[0::6])
            #Dentro de uma margem de 5 a 9, serão combinações de 3 espinhos:
            elif pontuação <= 9:
                combinação = choice(combinações_de_obstaculos[1::6])
                cor_base = [70, 85, 85]
                lista_elementos[0].cor = [200, 225, 255]
            #Dentro de uma margem de 10 a 14, serão combinações de 3 a 4 espinhos:
            elif pontuação <= 14:
                combinação = choice(combinações_de_obstaculos[1::6] + combinações_de_obstaculos[2::6])
                cor_base = [95, 75, 50]
                lista_elementos[0].cor = [230, 215, 180]
            #Dentro de uma margem de 15 a 19, serão combinações de 4 espinhos:
            elif pontuação <= 19:
                combinação = choice(combinações_de_obstaculos[2::6])
                cor_base = [80, 100, 55]
                lista_elementos[0].cor = [200, 235, 180]
            #Dentro de uma margem de 20 a 29, serão combinações de 4 a 5 espinhos:
            elif pontuação <= 29:
                combinação = choice(combinações_de_obstaculos[2::6] + combinações_de_obstaculos[3::6])
                if pontuação <= 24:
                    cor_base = [75, 60, 75]
                    lista_elementos[0].cor = [215, 200, 235]
                else:
                    cor_base = [255, 255, 255]
                    lista_elementos[0].cor = [85, 85, 85]
            #Dentro de uma margem de 30 a 59, serão combinações de 5 espinhos:
            elif pontuação <= 59:
                combinação = choice(combinações_de_obstaculos[3::6])
                if pontuação <= 34:
                    cor_base = [0, 150, 255]
                    lista_elementos[0].cor = [0, 115, 125]
                elif pontuação <= 39:
                    cor_base = [0, 255, 0]
                    lista_elementos[0].cor = [0, 115, 0]
                elif pontuação <= 44:
                    cor_base = [24, 24, 255]
                    lista_elementos[0].cor = [0, 0, 115]
                elif pontuação <= 49:
                    cor_base = [255, 0, 100]
                    lista_elementos[0].cor = [150, 0, 45]
                elif pontuação <= 54:
                    cor_base = [255, 255, 255]
                    lista_elementos[0].cor = [250, 165, 0]
                elif pontuação <= 59:
                    lista_elementos[0].cor = [0, 100, 255]
            #Dentro de uma margem de 60 a 199, serão combinações de 5 a 6 espinhos:
            elif pontuação <= 199:
                combinação = choice(combinações_de_obstaculos[3::6] + combinações_de_obstaculos[4::6])
                if pontuação <= 64:
                    lista_elementos[0].cor = [200, 0, 255]
                elif pontuação <= 69:
                    lista_elementos[0].cor = [0, 255, 0]
                elif pontuação <= 74:
                    lista_elementos[0].cor = [0, 0, 0]
                elif pontuação <= 79:
                    cor_base = [0, 0, 0]
                    lista_elementos[0].cor = [255, 115, 200]
                elif pontuação <= 84:
                    lista_elementos[0].cor = [120, 135, 255]
                elif pontuação <= 89:
                    lista_elementos[0].cor = [120, 255, 120]
                elif pontuação <= 94:
                    lista_elementos[0].cor = [150, 100, 255]
                elif pontuação <= 99:
                    lista_elementos[0].cor = [150, 185, 215]
                else:
                    cor_base = [255, 0, 0]
                    lista_elementos[0].cor = [0, 0, 0]
            #Dentro de uma margem de 200 a diante, serão combinações de 6 a 7 espinhos:
            else:
                combinação = choice(combinações_de_obstaculos[4::6] + combinações_de_obstaculos[5::6])

            #limpa a lista de espinhos que estão na tela:
            lista_de_obstaculos['espinhos'].clear()

            #Verifica o lado atual no qual os espinhos estão, caso seja direito:
            if lado_obstaculos:
                #Altera o lado dos espinhos:
                lado_obstaculos = False
                #Atribui as novas posições dos espinhos a ESQUERDA e os adiciona na lista de espinhos a serem mostrados na tela:
                for espinho_pos in combinação:
                    espinho_pos = posiçoes_espinhos['esquerda'][espinho_pos]
                    lista_de_obstaculos['espinhos'].append(imagens.Imagens(janela, espinhos_em_superficie['esquerda'].superficie, espinho_pos))
            #Caso seja esquerdo:
            else:
                #Altera o lado dos espinhos:
                lado_obstaculos = True
                #Atribui as novas posições dos espinhos a DIREITA e os adiciona na lista de espinhos a serem mostrados na tela:
                for espinho_pos in combinação:
                    espinho_pos = posiçoes_espinhos['direita'][espinho_pos]
                    lista_de_obstaculos['espinhos'].append(imagens.Imagens(janela, espinhos_em_superficie['direita'].superficie, espinho_pos))
            
            #Altera a cor dos espinhos com base na cor base:
            elementos.alterar_cor_conjunto_elementos(espinhos_em_superficie, cor_base)
            elementos.MostrarConjuntoElementos(espinhos_em_superficie)
            
            #Altera direção de voo do passaro:
            passaro.desloc[0] *= -1

        #COLISÃO COM BORDAS SUPERIORES E INFERIORES:
        elif passaro.posição[1] <= lista_elementos[0].posição[1] or passaro.posição[1] >= (lista_elementos[0].posição[1] + lista_elementos[0].posição[-1]):
            #Tocar som de morte
            pygame.mixer.Sound.play(sons['morte'])
            #O passaro morre e o jogo acaba:
            rodar_jogo = False
            break

        #COLISÃO COM ESPINHOS:
        #Itera o dicionario de espinhos na tela:
        for espinhos_list in lista_de_obstaculos.values():
            #Itera as listas de espinhos:
            for espinhos in espinhos_list:
                #Verifica se houve colisão entre o espinho e o passaro:
                colisão = mecanicas.colisao(passaro, espinhos)
                if colisão:
                    #Tocar som de morte
                    pygame.mixer.Sound.play(sons['morte'])
                    #O passaro morre e o jogo acaba:
                    rodar_jogo = False
                    break

        #FAZ O PASSARO ANDAR:
        passaro.deslocar_X()

        #ANIMAÇÃO DE PULO:
        #Verifica se o passaro pulou:
        if passaro.desloc[1] >= 0:
            #Altera o Sprite, para o sprite de pulo
            passaro.imagem = sprites['passaro'][0]
            #Caso o passaro pule o diminumento da velocidade do pulo diminui:
            diminuição = 0.30
        #Caso o passaro não tenha pulado, seu sprite ira mudar para o padrão:
        else:
            passaro.imagem = sprites['passaro'][1]

        #GRAVIDADE:
        #Caso o passaro tenha pulado, sua velocidade de pulo diminui e sua queda aumenta:
        passaro.desloc[1] += diminuição
        #Move o passaro em X:
        passaro.deslocar_Y()

        #MOSTRAR COMPONENTES DO JOGO:
        #Mostrar elementos:
        lista_elementos[0].mostrarElemento()
        lista_elementos[1].mostrarElemento()
        #Mostrar pontuação:
        pontuação_texto = fontes[0].render(f'{pontuação:0>2}', True, lista_elementos[0].cor)
        pos_pontuação = ((dimensões[0] / 2) - (pontuação_texto.get_width() / 2), (dimensões[1] / 2) - (pontuação_texto.get_height() / 2))
        janela.blit(pontuação_texto, pos_pontuação)
        #Mostrar o passaro:
        passaro.mostrarImagem()
        #Mostrar os espinhos:
        imagens.MostrarConjuntoImagens(lista_de_obstaculos)

        #ATUALIZA A JANELA:
        pygame.display.update()

        #LIMITA AS REPETIÇÕES POR SEGUNDO DO LOOP:
        relogio.tick(rps)        
