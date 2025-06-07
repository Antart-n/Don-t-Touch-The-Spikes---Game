'''
Facilita a manipulação e definição de parametros de imagens em Pygame.
'''

import pygame
from typing import Union


class Imagens:
    '''
    DESCRIÇÃO
    |    Facilita na manipulação e definição de uma determinada imagem.
    |
    '''
    def __init__(self, superficie: pygame.surface.Surface, imagem: pygame.surface.Surface, posição: list, desloc: list=[0, 0]):
        '''
        DESCRIÇÃO
        |    Define a imagem, superficie onde será mostrada, posição e deslocamento da imagem caso seja necessário.
        |    Além de facilitar na definição de parametros da imagem como: Mascara e Tamanho.
        |
        PARAMETROS
        |    param: superficie -> Surperficie onde a imagem será exibida:
        |    param: Imagem -> Define a imagem na qual será utilizada;
        |    param: posição -> Posição da imagem na superficie determinada;
        |    param: desloc -> Defini o deslocamento da imagem em x e y na superficie.
        '''
        self.superficie = superficie
        self.imagem = imagem
        self.posição = posição
        self.desloc = desloc
        self.mascara = pygame.mask.from_surface(self.imagem)
        
    
    def mostrarImagem(self):
        '''
        DESCRIÇÃO
        |    Exibe a imagem na superficie.
        |
        '''
        self.superficie.blit(self.imagem, self.posição)

    
    def deslocar_X(self):
        '''
        DESCRIÇÃO
        |    Desloca a posição de x da imagem na superficie.
        |
        '''
        self.posição[0] += self.desloc[0]

    def deslocar_Y(self):
        '''
        DESCRIÇÃO
        |    Desloca a posição de y da imagem na superficie.
        |
        '''
        self.posição[1] += self.desloc[1]


    def Definir_rect(self):
        '''
        DESCRIÇÃO
        |    Defini a posição Rect da imagem, atribuindo sua posição na superficie e pegando seu tamanho.
        |
        '''        
        self.posição = self.imagem.get_rect(topleft=tuple(self.posição))


def MostrarConjuntoImagens(Imagens: Union[list, tuple, set, dict]):
    '''
    DESCRIÇÃO
    |    Exibe um determinado conjunto de imagens
    |    (lista, tupla, dicionario ou conjuntos), em suas superficies.
    |
    PARAMETROS
    |    param: Imagens -> Lista, tupla, dicionario ou conjunto que armazenam as imagens.
    '''
    if type(Imagens) == list:
        for imagem in Imagens:
            imagem.mostrarImagem()

    elif type(Imagens) == set:
            for imagem in list(Imagens):
                imagem.mostrarImagem()
                
    elif type(Imagens) == dict:
        for imagem in Imagens.values():
            if type(imagem) == list or type(imagem) == set:
                for valor in list(imagem):
                    valor.mostrarImagem()
            else:
                imagem.mostrarImagem()


def espelhamento_conjunto_imagens(Imagens: Union[list, tuple, set, dict], espelhat_x: bool, espelhar_y: bool):
    '''
    DESCRIÇÃO
    |    Espelha um determinado conjunto de imagens
    |    (lista, tupla, dicionario ou conjuntos).
    |
    PARAMETROS
    |    param: Imagens -> Lista, tupla, dicionario ou conjunto que armazenam as imagens.
    |    param: espelhar -> Determina se a imagem será espelhada em x [0 = não] [1 = sim].
    |    param: espelhar -> Determina se a imagem será espelhada em y [0 = não] [1 = sim].
    '''
    if type(Imagens) in (list, set, tuple):
        for pos, imagem in enumerate(Imagens):
            Imagens[pos] = pygame.transform.flip(imagem, espelhat_x, espelhar_y)

    elif type(Imagens) == dict:
        if type(Imagens) in (list, set, tuple):
            Imagens = list(Imagens)
            for categoria, lista in Imagens.items():
                for pos, imagem in enumerate(lista):
                    Imagens[categoria][pos] = pygame.transform.flip(Imagens, espelhat_x, espelhar_y)

        else:
            for categoria, imagem in Imagens.items():
                Imagens[categoria] = pygame.transform.flip(imagem, espelhat_x, espelhar_y)
