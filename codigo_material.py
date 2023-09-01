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

