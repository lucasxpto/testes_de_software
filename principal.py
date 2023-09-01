"""
Claudinei de Oliveira - UTF8- pt-br - 18-88-2823
principal.py
"""
import readchar
# Importa o módulo readchar, que fornece
# uma função para ler um caracter por caractere
# na entrada padrão, sem a necessidade de pressionar
# a tecla Enter.

from validar_cpf import valida_cpf, mascara_cpf
# Importa a função valida_cpf do módulo test_cpf
# que é usada para verificar se um CPF é válido.


# Class App que conté a lógica do programa
class App:
    # Construtor da classe
    def __init__(self):
        pass

    # Método que lê a entrada do usuário
    # Caractere por caractere
    def get_user_input(self):
        cpf = ''  # Inicializa a variável cpf como um string vazia
        while True:  # Loop infinito
            char = readchar.readchar()  # Lê um caractere do teclado

            # Adiciona um contre para interromper a leitura se o número de caracteres do CPF exceder o l.
            if len(cpf) >= 14:
                break

            # Verifica se o caracter é um Enter
            if char == '\r' or char == '\n':
                # Se for, interrompe o loop
                break
            # Verifica se o caractere é um número
            elif char in '0123456789':
                # Se for, adiciona o caracter à variável cpf
                cpf += char
                cpf = mascara_cpf(cpf)  # Aplica a máscara do CPF

            # Verifica se o caractere é um Backspace e se há caracteres no CPF
            elif char == '\x7f' and cpf:
                # Se for, remove o último caractere do CPF
                cpf = cpf[:-1]

            # Imprime o cpf form na mesma linha
            print(f'\rDigite o CPF do cliente (ou pressione Enter para encerrar): {cpf}', end='', flush=True)

        # Retorna o CPF formatado
        return cpf

    # Método que pede o CPF ao usuário e verifica se é válido
    def pede_cpf(self):
        # Inicia o loop infinito
        while True:
            # Solicita o CPF ao usuário
            print('Digite o CPF do cliente (ou pressione Enter para encerrar): ', end='', flush=True)
            # Lê o CPF do usuário
            cpf = self.get_user_input()

            # Verifica se o cpf está vazio
            if not cpf:
                # Se estiver, encerra o programa
                print('Encerrando o programa...')
                break

            # Verifica se o CPF é válido
            elif valida_cpf(cpf):
                # Se for válido, imprime uma mensagem de sucesso
                print(f'\nCPF válido: {cpf}! Continue com a operação!!!')
            else:
                # Se for inválido, imprime uma mensagem de erro
                print(f'\nCPF inválido: {cpf}! Por favor, tente novamente!!!')
        

# Se este arquivo for o ponto de entrada do programa
if __name__ == '__main__':
    # Cria uma instância da classe App
    app = App()
    # Executa a função que pede o CPF ao usuário
    app.pede_cpf()
