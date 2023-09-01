"""
Claudinei de Oliveira - UTF8 - pt-br - 18-08-2023
testa_cpf.py
"""

# código importa o módulo re (que representa "expressões regulares")
# da biblioteca padrão do Python - que são chamadas de regex
# Expressões regulares, podem ser usadas para pesquisar, combinar e
#manipular texto de maneira complexa e flexível

import re

# Esta define a função chamada valida_cpf que tem um parametro chamado cpf
def valida_cpf(cpf):

    # Verifica se um CPF é válido.
    # tem como parâmero: uma string representando um CPF
    # e retorna True se o CPF for válido, False se inválido

    # Remove caracteres não numéricos do CPF
    cpf=''.join(re.findall(r'\d', cpf))

    # Verifica se o CPF tem 11 digitos
    if len(cpf) != 11:
        return False

    # Verifica se o CPF tem todos os digitos iguals (inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calcula os digitos verificadores do CPF
    def calcula_digito(d):

        # Calcula o digito verificador de um CPF
        # soma dos produtos dos digitos do CPF por um peso especifico
        # retorna o digito verificador.

        return (11 - d % 11) % 10

    # Calcula o primeiro digito verificador
    digito1 = sum(i * int(cpf[idx]) for idx, i in enumerate(range(10, 1, -1)))

    # Calcula o segundo digito verificador (incluindo o primeiro digito verificador)
    digito2 = sum(i * int(cpf[idx]) for idx, i in enumerate(range(11, 1, -1)))

    # Retorna True se os digitos calculados correspondem aos digitos do CPF
    return  cpf[-2:] == f'{calcula_digito(digito1)}{calcula_digito(digito2)}'

 # Separando a mascara do CPF
def mascara_cpf(cpf: str) -> str:
    n = len(cpf.replace('.', '').replace('-', ''))  # Conta a quantidade de caracteres no CPF sem pontuação
    if n == 3 or n == 6:
        # Se o CPF tem 3 ou 6 caracteres sem a pontuação, adiciona um ponto
        cpf += '.'
    elif n == 9:
        # Se o CPF tem 9 caracteres sem a pontuação, adiciona um hífen
        cpf += '-'
    return cpf  # Retorna o CPF com a máscara