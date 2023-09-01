"""
Claudinei de Oliveira - UTF8- pt-br - 18-88-2823
Aluno: Lucas Pedreira Vital
principal.py
"""
import readchar
from validar_cpf import valida_cpf, mascara_cpf
import time

class App:
    def __init__(self):
        pass

    def get_user_input(self):
        # Inicializa a variável que armazenará o CPF
        cpf = ''
        # Inicializa a variável que armazenará o CPF formatado
        cpf_formatado = ''
        cursor_pos = 0  # Posição do cursor na string
        # Prompt que será exibido ao usuário
        prompt = 'Digite o CPF do cliente (ou pressione Enter para encerrar): '

        while True: # loop infinito
            # Lê um caractere digitado pelo usuário
            char = readchar.readchar()
            # se o tamanho do CPF for maior ou igual a 11, encerra o loop
            if len(cpf) >= 11:
                break
            # Encerra o programa se o usuário pressionar Enter sem digitar nada    
            if char == '\r' or char == '\n':  # Tecla Enter
                break
                # Se o caractere digitado for um número, adiciona-o ao CPF
            elif char in '0123456789':  # Teclas numéricas
                # Insere o caractere na posição do cursor
                cpf = cpf[:cursor_pos] + char + cpf[cursor_pos:]
                # Incrementa a posição do cursor
                cursor_pos += 1

            # Após a inserção completa do CPF, 'backspace' age como 'Enter'.
            elif char == '\x7f' and len(cpf) == 11:
                break

            elif char == '\x7f' and cursor_pos > 0:  # Tecle backspace
                # Remove o caractere anterior à posição do cursor
                cpf = cpf[:cursor_pos-1] + cpf[cursor_pos:]
                # Decrementa a posição do cursor
                cursor_pos -= 1

            elif char == '\x1b':  # Seta para esquerda ou direita
                # Lê os próximos dois caracteres
                next1, next2 = readchar.readchar(), readchar.readchar()
                # Se for uma seta para esquerda, decrementa a posição do cursor
                if next1 == '[':
                    if next2 == 'D':  # Seta para esquerda
                        cursor_pos = max(0, cursor_pos - 1)
                    elif next2 == 'C':  # Seta para direita
                        cursor_pos = min(len(cpf), cursor_pos + 1)
                    elif next2 == '3':  # Delete
                        next3 = readchar.readchar()  # Le a parte final da sequencia
                        if next3 == '~':  # Confirma que é o delete
                            if cursor_pos < len(cpf): # Se o cursor não estiver no final da string
                                # Remove o caractere na posição do cursor
                                cpf = cpf[:cursor_pos] + cpf[cursor_pos+1:]

            cpf_formatado = mascara_cpf(cpf) # Formata o CPF
            # Limpa a linha atual
            print('\r\033[K', end='')
            # Imprime o CPF atualizado
            print(f'{prompt}{cpf_formatado}', end='')
            # Coloca o cursor na posição correta
            ajusta_posicao_cursor = cursor_pos + cpf_formatado.count('.') + cpf_formatado.count('-')

            # Move o cursor para a posição correta
            print(f'\033[{len(prompt) + ajusta_posicao_cursor}G', end='', flush=True)
        return cpf_formatado # Retorna o CPF formatado

    def pede_cpf(self):
        while True:
            # Prompt que será exibido ao usuário
            print('Digite o CPF do cliente (ou pressione Enter para encerrar): ', end='', flush=True)
            # Chama a função get_user_input para obter o CPF digitado pelo usuário
            cpf = self.get_user_input()

            if not cpf: # Se o usuário pressionou Enter sem digitar nada
                print('Encerrando o programa...')
                break

            if valida_cpf(cpf): # Se o CPF for válido
                print(f'\nCPF válido: {cpf}! Continue com a operação!!!')
            else:
                # Se o CPF for inválido
                print(f'\nCPF inválido: {cpf}! Por favor, tente novamente!!!')
                time.sleep(1) # Aguarda 1 segundo antes de continuar

if __name__ == '__main__':
    # Instancia a classe App
    app = App()
    # Chama o método pede_cpf
    app.pede_cpf()
