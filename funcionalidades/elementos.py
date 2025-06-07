'''
Facilita a manipulação e definição de parâmetros de elementos/formas como: circulos, retangulos e triangulos em Pygame.
'''

import pygame
from typing import Union

class Elementos:
    '''
    DESCRIÇÃO
    |    Facilita na manipulação e definição de um determinado elemento/forma.
    |
    '''
    def __init__(self, superficie: pygame.Surface, tipo: str, cor: Union[list, tuple], posição: Union[list, tuple], raio: int=10, preenchimento: int=0):
        '''
        DESCRIÇÃO
        |    Define parametros importantes de um elemento/forma,
        |    como: Superficie onde será desenhada, Tipo de forma, Cor da forma, 
        |    posição, raio (caso a forma seja um circulo) e preenchimento da forma.
        |
        PARAMETROS
        |    param: superficie -> Superficie onde o elemento/forma será desenhada;
        |    param: tipo -> Tipo de forma a ser desenhada;
        |    param: cor -> Cor da forma;
        |    param: posição -> Posição da forma na superficie determinada;
        |    param: raio -> Define o raio do circulo, caso a forma seja um circulo;
        |    param: preenchimento -> Define o preenchimento ou contorno da borda da forma determinada.
        '''
        self.superficie = superficie
        self.tipo = tipo
        self.cor = cor
        self.posição = posição
        self.raio = raio
        self.preenchimento = preenchimento
        
    
    def mostrarElemento(self):
        '''
        DESCRIÇÃO
        |    Exibe o elemento/forma na superficie.
        |
        '''
        if self.tipo == 'rect':
            pygame.draw.rect(self.superficie, self.cor, self.posição, self.preenchimento)
        elif self.tipo == 'polygon':
            pygame.draw.polygon(self.superficie, self.cor, self.posição, self.preenchimento)
        elif self.tipo == 'circle':
            pygame.draw.circle(self.superficie, self.cor, self.posição, self.raio, self.preenchimento)


def alterar_cor_conjunto_elementos(Elementos: Union[list, dict, set], cor: list):
    '''
    DESCRIÇÃO
    |    Altera a cor de um conjunto (lista, tupla, dicionario, conjuntos) de elementos/formas
    |    para uma cor determinada.
    |
    PARAMETROS
    |    param: Elementos -> Conjuntos de elementos/formas que terão suas cores alteradas;
    |    param: cor -> Cor para a qual serão alteradas as cores dos elementos/formas.
    '''
    if type(Elementos) in (list, set, tuple):
        for pos, elemento in enumerate(Elementos):
            Elementos[pos].cor = cor

    elif type(Elementos) == dict:
        for categoria, lista in Elementos.items():
            if type(lista) in (list, set, tuple):
                lista = list(lista)
                for pos, elemento in enumerate(lista):
                    Elementos[categoria][pos].cor = cor
            else:
                for categoria in Elementos.keys():
                    Elementos[categoria].cor = cor


def MostrarConjuntoElementos(Elementos: Union[list, dict, set]):
    '''
    DESCRIÇÃO
    |    Exibi um determinado conjunto de elementos/formas
    |    (lista, tupla, dicionario ou conjuntos), em suas superficies.
    |
    PARAMETROS
    |    param: Elementos -> Lista, tupla, dicionario ou conjunto que armazenam os elementos/formas.
    '''
    if type(Elementos) == list:
            for elemento in Elementos:
                elemento.mostrarElemento()

    elif type(Elementos) == set:
            for elemento in list(Elementos):
                elemento.mostrarElemento()
                
    elif type(Elementos) == dict:
        for elemento in Elementos.values():
            if type(elemento) == list or type(elemento) == set:
                for valor in list(elemento):
                    valor.mostrarElemento()
            else:
                elemento.mostrarElemento()


def redimensionar_lista_elementos(list_Elementos: list, escala: Union[list, tuple]):
    '''
    DESCRIÇÃO
    |    redimensiona o tamanho dos elementos em uma lista de elementos/formas.
    |    
    PARAMETROS
    |    param: lista_Elementos -> Lista de elementos/formas;
    |    param: escala -> Lista ou Tupla com as posições para a qual os elementos serão redimensionadas.
    '''
    for pos, elemento in enumerate(list_Elementos):
        list_Elementos[pos] = pygame.transform.scale(elemento, escala)
