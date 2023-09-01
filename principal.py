"""
Claudinei de Oliveira - UTF8- pt-br - 18-88-2823
Aluno: Lucas Pedreira Vital
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
# Importa a função mascara_cpf do módulo test_cpf

# Class App que conté a lógica do programa
class App:
    # Construtor da classe
    def __init__(self):
        pass

    # Método que lê a entrada do usuário
    # Caractere por caractere
    def get_user_input(self):
        cpf = '' # Inicializa a variável cpf como um string vazia
        while True: # Loop infinito
            char = readchar.readchar() # Lê um caractere do teclado

            # Adiciona um contre para interromper a leitura 
            # se o número de caracteres do CPF exceder o limite
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
                cpf = mascara_cpf(cpf) # Aplica a máscara de CPF

            # Verifica se o caractere é um Backspace e se há caracteres no CPF
            elif char == '\x7f' and len(cpf) > 0:  # usando '\x7f' para representar o BACKSPACE
                # Se for, remove o último caracter da variável cpf
                cpf = cpf[:-1]

            # Limpa a linha e reimprime a linha com o novo valor (cpf)
            print('\r\033[K', end='')  # \033[K limpa até o final da linha
            # Imprime a linha com o novo valor (cpf)
            print(f'Digite o CPF do cliente (ou pressione Enter para encerrar): {cpf}', end='', flush=True)

        # retorna o CPF formatado
        return cpf

    # Método que pede o CPF ao usuário e verifica se é válido
    def pede_cpf(self):
        # Inicia o loop infinito
        while True:
            # Solicita o CPF ao usuário
            print('Digite o CPF do cliente (ou pressione Enter para encerrar): ', end='', flush=True)
            # Lê o CPF do usuário
            cpf = self.get_user_input()
            print('')  # imprime uma linha depois do input

            # Verifica se o cpf está vazio
            if not cpf:
                # Se estiver, encerra o programa
                print('Encerrando o programa...')
                break
            # Verifica se o CPF é válido
            if valida_cpf(cpf):
                # Se for válido, imprime uma mensagem de sucesso
                print(f'CPF válido: {cpf}! Continue com a operação!!!')
            else:
                # Se for inválido, imprime uma mensagem de erro
                print(f'CPF inválido: {cpf}! Por favor, tente novamente!!!')

# Se este arquivo for o ponto de entrada do programa
if __name__ == '__main__':
    # Cria uma instância da classe App
    app = App()
    # Chama o método pede_cpf da instância app
    app.pede_cpf()
