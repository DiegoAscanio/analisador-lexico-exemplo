#!/usr/bin/env python
# A função do analisador léxico é a de analisar um arquivo contendo um programa e retornar na ordem crescente de leitura os lexemas de uma linguagem contendo, para cada lexema, um token (uma tupla) com seus símbolos terminais ("program", "sum", "=", ...) e o tipo do lexema lido (TokenType)

# Um automato de estados finitos (disponível em: https:#raw.githubusercontent.com/rimsa/tiny/master/images/lexico.png) é um mecanismo que é capaz de ler um token e retornar a tupla (SIMBOLO_TERMINAL,TokenType). Esse automato de estados finitos é implementado na função next_token e ele deve ser chamado pelo analisador léxico até que um token do tipo END_OF_FILE, UNEXPECTED_EOF ou INVALID_TOKEN tenha sido lido. Durante sua execução, o analisador léxico deve imprimir uma lista contendo todos os tokens lidos.

# É conveniente que o analisador léxico receba como único parametro o arquivo do programa a ser lido.

# O analisador léxico deve manter o controle do cabeçote de leitura (indice de qual caractere está sendo lido) do arquivo e deve conseguir avançar ou retroceder a leitura do arquivo, com o apoio das funções avancar e retroceder.

# A funcao avancar retorna o caractere da posicao corrente do cabeçote e incrementa o cabecote em um

# A funcao retroceder apenas decrementa (em um) o cabecote de leitura.

# Uma tabela de símbolos existe para nos auxiliar a tratar os tokens que representam palavras (e operações) reservadas da linguagem.

import pdb
import sys
from enum import Enum

TipoToken = Enum(
    'TipoToken', [
        # Specials
        'UNEXPECTED_EOF',
        'INVALID_TOKEN',
        'END_OF_FILE',
    
        # Symbols
        'SEMICOLON',     # ;
        'ASSIGN',        # =
    
        # Logic operators
        'EQUAL',         # ==
        'NOT_EQUAL',     # !=
        'LOWER',         # <
        'LOWER_EQUAL',   # <=
        'GREATER',       # >
        'GREATER_EQUAL', # >=
    
        # Arithmetic operators
        'ADD',           # +
        'SUB',           # -
        'MUL',           # *
        'DIV',           # /
        'MOD',           # %
    
        # Keywords
        'PROGRAM',       # program
        'WHILE',         # while
        'DO',            # do
        'DONE',          # done
        'IF',            # if
        'THEN',          # then
        'ELSE',          # else
        'OUTPUT',        # output
        'TRUE',          # true
        'FALSE',         # false
        'READ',          # read
        'NOT',           # not
    
        # Others
        'NUMBER',        # number
        'VAR'            # variable
    ]
)

tabela_simbolos = {
    # simbolos
    ';': TipoToken.SEMICOLON,
    '=': TipoToken.ASSIGN,

    # operadores logicos
    '==': TipoToken.EQUAL,
    '!=': TipoToken.NOT_EQUAL,
    '<':  TipoToken.LOWER,
    '<=': TipoToken.LOWER_EQUAL,
    '>':  TipoToken.GREATER,
    '>=': TipoToken.GREATER_EQUAL,

    # operadores aritmeticos
    '+': TipoToken.ADD,
    '-': TipoToken.SUB,
    '*': TipoToken.MUL,
    '/': TipoToken.DIV,
    '%': TipoToken.MOD,

    # palavras-chave
    'program': TipoToken.PROGRAM,
    'while': TipoToken.WHILE,
    'do': TipoToken.DO,
    'done': TipoToken.DONE,
    'if': TipoToken.IF,
    'then': TipoToken.THEN,
    'else': TipoToken.ELSE,
    'output': TipoToken.OUTPUT,
    'true': TipoToken.TRUE,
    'false': TipoToken.FALSE,
    'read': TipoToken.READ,
    'not': TipoToken.NOT,
}

programa = ''
simbolo_terminal = ''
cabecote = 0
linhas = 0

def ler_programa(caminho_arquivo: str):
    global programa
    try:
        with open(caminho_arquivo, 'r') as f:
            programa = f.read()
    except FileNotFoundError as fe:
        raise Exception('O arquivo {} não foi encontrado!'.format(caminho_arquivo))

def avancar() -> str:
    global cabecote
    try:
        caractere = programa[cabecote]
        cabecote += 1
    except IndexError as ie: # chegou ao caractere final do programa, portanto, caractere deve ser vazio
        caractere = ''
    return caractere

def retroceder(c):
    global cabecote
    if c != '':
        cabecote -= 1

# apenas o processamento do estado 1, com suas respectivas transições a depender do valor de c, são implementadas para fins de explicação
# neste código do analisador. Os demais estados, vocês devem implementar se usarem este código como modelo.

def processar_estado_1(c):
    global simbolo_terminal
    global linhas
    if c == ' ' or c == '\r' or c == '\t':
        return estados.inicial
    elif c == '\n':
        linhas += 1
        return estados.inicial
    elif c == '#':
        return estados.ler_comentarios
    elif c == '=' or c == '<' or c == '>':
        simbolo_terminal += c
        return estados.ler_atribuicao_comparacao_ou_igualdade
    elif c == '!':
        simbolo_terminal += c
        return estados.ler_nao_igual
    elif c == ';' or c == '+' or c == '-' or c == '*' or c == '/' or c == '%':
        simbolo_terminal += c
        return estados.criar_token_reservado_ou_variavel
    elif c.isalpha() or c == '_':
        simbolo_terminal += c
        return estados.ler_variavel
    elif c.isdigit():
        simbolo_terminal += c
        return estados.ler_digito
    elif c == '':
        return estados.criar_token_fim_de_arquivo
    else:
        simbolo_terminal += c
        return estados.criar_token_invalido

# implementar processar_estado do 2 até o 11

def processar_estado_2(c):
    global linhas
    pass

def processar_estado_3(c):
    global linhas
    global simbolo_terminal
    pass

def processar_estado_4(c):
    global linhas
    global simbolo_terminal
    pass

def processar_estado_5(c):
    global linhas
    global simbolo_terminal
    pass

def processar_estado_6(c):
    global linhas
    global simbolo_terminal
    pass

def processar_estado_7():
    global simbolo_terminal
    pass

def processar_estado_8():
    global simbolo_terminal
    pass

def processar_estado_9():
    global simbolo_terminal
    pass

def processar_estado_10():
    global simbolo_terminal
    pass

def processar_estado_11():
    global simbolo_terminal
    pass

# estados do automato de leitura de tokens
# explicito é melhor que implicito!
estados = Enum('estados', [
    'inicial', # 1 - o estado onde o automato começa e se mantem ao ler espaços em branco e novas linhas
    'ler_comentarios', # 2 - o estado que representa a leitura de comentarios, o automato continua nele até ler uma nova linhas
    'ler_atribuicao_comparacao_ou_igualdade', # 3 - o estado que representa a leitura de uma atribuicao (=) ou comparacao (>, <, >=, <=, ==)
    'ler_nao_igual', # 4 - o estado subsequente à leitura da exclamação (!) que só possui transição válida para um caractere igual
    'ler_variavel', # 5 o estado para o qual o automato transita (a partir de 1) quando le uma letra ou underscore
    'ler_digito', # o estado para o qual o automato transita (à partir de 1) quando le um digito
    'criar_token_reservado_ou_variavel', # no estado 7, deve ser realizada uma consulta a tabela de simbolos para, depois da extração do lexema, verificar se ele é uma palavra reservada da linguagem ou uma variável, aqui a tupla (token, tipotoken) é criada, sendo uma variável (TipoToken.VAR) ou uma palavra reservada da linguagem
    'criar_token_numerico', # o estado 8 vem de uma transição do estado 6, onde ocorre a leitura de digitos, neste estado, quando ocorre a finalização da leitura de digitos, é criado uma tupla (token, TipoToken.NUM).
    'criar_token_fim_de_arquivo_nao_esperado', # qualquer estado pode transitar para este quando encontra um fim de arquivo nao esperado
    'criar_token_invalido', # qualquer estado pode transitar para este quando processa algum lexema inválido
    'criar_token_fim_de_arquivo', # se o estado pode processar um fim de arquivo valido, então, transita para cá
    ]
)

''' 
# Dicionario de funcoes, deixa o codigo de proximo token mais enxuto e legível, desabilitado por que mostrei aqui como se fazer com if
# para se tornar mais genérico como modelo para outras linguagens
AFD = {
    estados.inicial: processar_estado_1,
    estados.ler_comentarios: processar_estado_2,
    estados.ler_atribuicao_comparacao_ou_igualdade: processar_estado_3,
    estados.ler_nao_igual: processar_estado_4,
    estados.ler_variavel: processar_estado_5,
    estados.ler_digito: processar_estado_6,
    estados.criar_token_reservado_ou_variavel: processar_estado_7,
    estados.criar_token_numerico: processar_estado_8,
    estados.criar_token_fim_de_arquivo_nao_esperado: processar_estado_9,
    estados.criar_token_invalido: processar_estado_10,
    estados.criar_token_fim_de_arquivo: processar_estado_11
}
'''

def proximo_token():
    global simbolo_terminal
    simbolo_terminal = ''
    estado = estados.inicial
    while estado != estados.criar_token_reservado_ou_variavel and estado != estados.criar_token_numerico and estado != estados.criar_token_fim_de_arquivo_nao_esperado and estado != estados.criar_token_invalido and estado != estados.criar_token_fim_de_arquivo:
        # proximo caractere
        c = avancar()
        # explicito é melhor do que implicito
        if estado == estados.inicial:
            estado = processar_estado_1(c)
        elif estado == estados.ler_comentarios:
            estado = processar_estado_2(c)
        elif estado == estados.ler_atribuicao_comparacao_ou_igualdade:
            estado = processar_estado_3(c)
        elif estado == estados.ler_nao_igual:
            estado = processar_estado_4(c)
        elif estado == estados.ler_variavel:
            estado = processar_estado_5(c)
        elif estado == estados.ler_digito:
            estado = processar_estado_6(c)
    if estado == estado.criar_token_reservado_ou_variavel:
        lexema = processar_estado_7()
    elif estado == estado.criar_token_numerico:
        lexema = processar_estado_8()
    elif estado == estado.criar_token_fim_de_arquivo_nao_esperado:
        lexema = processar_estado_9()
    elif estado == estado.criar_token_fim_de_arquivo:
        lexema = processar_estado_11()
    else: # token invalido
        lexema = processar_estado_10()

    return lexema


def analisador_lexico():
    global linhas
    token, tipo = proximo_token()
    while tipo != TipoToken.END_OF_FILE and tipo != TipoToken.INVALID_TOKEN and tipo != TipoToken.UNEXPECTED_EOF:
        print((token, tipo))
        token, tipo = proximo_token()
    if tipo == TipoToken.END_OF_FILE:
        print((token, tipo))
    elif tipo == TipoToken.INVALID_TOKEN:
        print('Linha {:02d} Lexema Inválido {}'.format(linhas, token))
    elif tipo == TipoToken.UNEXPECTED_EOF:
        print('Linha {:02d} Fim de arquivo inesperado'.format(linhas))


# A funcao retorna verdadeiro e o caminho do programa quando o programa apresenta um formato valido (.tiny) ou falso e uma mensagem de erro quando o programa não possui formato ou um formato invalido
# Explicito é melhor que implicito
def arquivo_programa_valido() :
    if len(sys.argv) != 2:
        return False, 'Você não carregou o programa! O uso correto é: ./analisador_lexico.py <programa.tiny>'
    try:
        caminho_arquivo, formato = sys.argv[1].split('.')
    except ValueError:
        return False, 'O arquivo informado não possui formato'
    if formato != 'tiny':
        return False, 'O interpretador interpreta somente arquivos tiny'

    return True, sys.argv[1]

def main():
    programa_valido, informacao = arquivo_programa_valido()
    if programa_valido:
        try:
            ler_programa(informacao)
            analisador_lexico()
        except Exception as e:
            raise e
    else:
        raise Exception('Erro: {}'.format(informacao))

if __name__ == '__main__':
    main()
