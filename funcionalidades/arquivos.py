'''
Facilita tarefas em tratamento de arquivos.
'''

def verificar_arquivo(nome_arquivo: str, texto: str):
    '''
    DESCRIÇÃO
    |    Verifica se o arquivo inserido existe, caso o arquivo não
    |    exista ele criara um novo e irá atribuir o valor pré-definido.
    |
    PARAMETROS
    |    param: nome_arquivo -> Nome do arquivo que deseja verificar;
    |    param: texto -> Texto a ser adicionado caso o arquivo não exista.
    '''
    try:
        arquivo = open(nome_arquivo, 'r')
    except:
        arquivo = open(nome_arquivo, 'w')
        arquivo.write(texto)
    finally:
        arquivo.close()
