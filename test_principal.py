"""
Claudinei de Oliveira - UTF8 pt-br - 18-08-2023
test_principal.py
"""


# Importa o módulo de testes unitários do Python,
# o unittest, que fornece uma estrutura para criar  e
# executar testes unitários em código Python
import unittest

# Importa a função valida_cpf do módulo testa_cpf,
# que é a função que verifica se um número de CPF é válido.
from validar_cpf import valida_cpf, mascara_cpf


# Definição da classe de teste para a função valida_cpf
class TestValidaCpf(unittest.TestCase):
    # Teste de unidade que verifica se a função valida_cpf reconhece corretamente um CPF válido
    def test_valida_cpf_valido(self):
        # Verifica se a função valida_cpf retorna True para um CPF válido
        # Para testar: usamos CPF "529.982.247-25", que é um CPF válido
        # A função deve retornar True para indicar que reconheceu o CPF como válido.
        self.assertTrue(valida_cpf('52998224725'), 'A função não validou corretamente um CPF válido.')

    # Teste de unidade que verifica se a função valida_cpf reconhece corretamente um CPF inválido
    def test_valida_cpf_invalido(self):
        # verifica se a função valida_cpf retorna False para um CPF invalido # CPF "111.111.111-11", é um CPF inválido.
        # este método deve retornar False para indicar que reconheceu o CPF como inválido
        self.assertFalse(valida_cpf('11111111111'), 'A função não reconheceu corretamente um CPF inválido.')

    # Início  para os testes para a mascara do CPF
    def test_mascara_cpf(self):
        # Verifica se a função mascara_cpf retorna a máscara correta para um CPF com 3 dígitos
        assert mascara_cpf("123") == "123." 
        # Verifica se a função mascara_cpf retorna a máscara correta para um CPF com 6 dígitos
        assert mascara_cpf("123.456") == "123.456." 
        # Verifica se a função mascara_cpf retorna a máscara correta para um CPF com 9 dígitos
        assert mascara_cpf("123.456.789") == "123.456.789-"
        # Verifica se a função mascara_cpf retorna a máscara correta para um CPF com 10 dígitos
        assert mascara_cpf("123.456.789-0") == "123.456.789-0"
        # Verifica se a função mascara_cpf retorna a máscara correta para um CPF completo
        assert mascara_cpf("123.456.789-01") == "123.456.789-01"




# Verifica se este arquivo é o ponto de entrada do programa
if __name__ == '__main__':
    # Se for, inicia a execução dos testes de unidade
    unittest.main()
