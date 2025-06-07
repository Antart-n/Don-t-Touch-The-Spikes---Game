'''
Simplifica as mecanicas do jogo atribuindo elas a funções separadas.
'''

import pygame
import copy
from typing import Union


def colisao(elemento1: pygame.surface.Surface, elemento2: pygame.surface.Surface):
    '''
    DESCRIÇÃO
    |    Verifica a colisão entre dois objetos (pygame.surface.Surface) e retorna a colisão.
    |
    PARAMETROS
    |    param: elemento1 -> Primeiro objeto pygame.surface.Surface;
    |    param: elemento2 -> Segundo objeto pygame.surface.Surface.
    '''
    desvio = (int(elemento1.posição[0] - elemento2.posição[0]), int(elemento1.posição[1] - elemento2.posição[1]))
    colisão = elemento2.mascara.overlap(elemento1.mascara, desvio)
    return colisão
    

def criarListaPosiçoes(posição_base: list, tamanho: int, deslocamento: Union[int, float], direção: bool):
    '''
    DESCRIÇÃO
    |    Cria uma lista com posições em seguencia com base em uma posição principal.
    |
    PARAMETROS
    |    param: posição_base -> Posição base para as outras posições;
    |    param: tamanho -> Número de posições novas a serem criadas e adicionada a lista;
    |    param: deslocamento -> Deslocamento entre cada posição.
    |    param: direção -> define se a direção do deslocamento é no eixo x ou y, na qual a posição será deslocada.
    '''
    lista_posições = []
    for repetição in range(tamanho):
        posição_base[direção] += deslocamento
        lista_posições.append(copy.deepcopy(posição_base))

    return lista_posições
