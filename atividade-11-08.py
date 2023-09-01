# Exercícios unittest:
# Lucas Pedreira Vital

import unittest

# a)

"""

class Elefante:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    def som(self):
        return f"O {self._nome} está trombeteando"


elefante = Elefante("elefante")

# Erro ao acessar diretamente fora da classe
# print(elefante._nome)

print(elefante.nome)  # Utilizando a propriedade nome
print(elefante.som())  # Exibirá: O elefante está trombeteando


class TestElefante(unittest.TestCase):

    def setUp(self):
        self.elefante = Elefante("elefante")

    def test_nome(self):
        self.assertEqual(self.elefante.nome, "elefante")

    def test_som(self):
        self.assertEqual(self.elefante.som(), "O elefante está trombeteando")


if __name__ == '__main__':
    unittest.main()
    
"""


# b)


"""

def converter_data(data_str):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
             "agosto", "setembro", "outubro", "novembro", "dezembro"]

    dia, mes, ano = data_str.split("/")
    mes_formatado = meses[int(mes) - 1]  # -1 pois listas são indexadas a partir de 0

    return f"{dia} de {mes_formatado} de {ano}"


def main():
    data_usuario = input("Digite uma data no formato dd/mm/aaaa: ")
    data_formatada = converter_data(data_usuario)
    print(f"Ariquemes, {data_formatada}.")


class TestDataConverter(unittest.TestCase):

    def test_converter_data(self):
        self.assertEqual(converter_data("23/03/2023"), "23 de março de 2023")
        self.assertEqual(converter_data("01/01/2000"), "01 de janeiro de 2000")


if __name__ == "__main__":
    escolha = input("Deseja rodar o programa ou unittest (escolha 'programa' ou 'unittest')? ")

    if escolha.lower() == 'programa':
        main()
    elif escolha.lower() == 'unittest':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        print("Opção não reconhecida.")


"""


# c)

"""
class Calculadora:

    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return None
        return a / b


def test_adicionar():
    calc = Calculadora()
    assert calc.adicionar(5, 3) == 8
    assert calc.adicionar(-5, 3) == -2
    assert calc.adicionar(0, 0) == 0


def test_subtrair():
    calc = Calculadora()
    assert calc.subtrair(5, 3) == 2
    assert calc.subtrair(3, 5) == -2
    assert calc.subtrair(0, 0) == 0


def test_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(5, 3) == 15
    assert calc.multiplicar(-5, 3) == -15
    assert calc.multiplicar(0, 5) == 0


def test_dividir():
    calc = Calculadora()
    assert calc.dividir(6, 3) == 2
    assert calc.dividir(-6, 3) == -2
    assert calc.dividir(0, 5) == 0
    assert calc.dividir(5, 0) == None

"""

# pip install pytest
# pytest atividade-11-08.py


# -------------------------------------------------
# CÓDIGO DO MATERIAL DE APOIO
# -------------------------------------------------

"""

# Definindo a classe Pessoa.
class Pessoa:

    def __init__(self, nome, sobrenome):
        # Atribuindo os parâmetros nome e sobrenome às
        # variáveis de instância da classe.
        self.nome = nome
        self.sobrenome = sobrenome
        # Método para obter o nome completo da pessoa.

    def get_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


# Importando o módulo unittest que fornece infraestrutura
# para escrever testes unitários.
import unittest


# Definindo a classe de teste que herda de unittest.TestCase.
class TestPessoa (unittest.TestCase):

    # Método de teste para verificar a corretude do método
    # get_nome_completo.
    def test_obter_nome_completo(self):
        # Criando uma instância da classe Pessoa.
        p = Pessoa('Fulano', 'Filó')
        # Verificando se o método get nome completo retorna o valor esperado.
        # Se o valor retornado não for "Filomena", a teste falhará.
        self.assertEqual('Filomena Filó', p.get_nome_completo())


# Verificando se este script está sendo executado como o programa principal.
if __name__ == '__main__':
    # Se for o caso, executa os testes definidos neste módulo.
    unittest.main()


# Método assertEqual
# import unittest
class TestExample (unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()


# Aplicando unitest com Pytest:
# Importação da biblioteca pytest
import pytest


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def get_nome_completo (self):
        return f'{self.nome} {self.sobrenome}'


# Pytest
def test_obter_nome_completo():
    # Testa se a função get_nome_completo retorna o nome completo
    p = Pessoa('Fulano', 'Filó')
    # O pytest utiliza a instrução assert para fazer as verificações
    assert p.get_nome_completo() == 'Fulano Filó', f'Erro: {p.get_nome_completo()}'


# O bloco abaixo permite executar os testes com o comando python nome_do_arquivo.py
if __name__ == '_main__':
    # pytest.main() executa todos os testes no script
    pytest.main([__file__])
    
"""


