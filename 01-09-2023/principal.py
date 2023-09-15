import curses # Importa o módulo curses para interface do terminal
import time # Importa para usar a função sleep
from testa_cpf import valida_cpf # Importa a função de validação aqui

class App: # define classe chanada App
    def __init__(self, stdscr): # define o método __init__
        #Inicializando a tela do curses
        self.stdscr = stdscr # É una referência ao objeto que está sendo criado
                            # stdscr é un parametro que deve ser fornecido quando
                            # crianos un novo objeto da classe App
            # 0 nome sugere que ele poderia ser uma "tela padrão", possivelmente 
            # um objeto de tela para alguma biblioteca de interface do usuário, 
            # como o curses no Python
        self.run() # Executa a lógica principal

    def get_user_input(self, prev_input=''): # define o método
                                            #get_user_input: é o nome do método que 
                                            # está sendo definido, o none sugere 
                                            # que este método será utilizado para obter algun tipo de entrada do usuário 
                                            # (self, prev_input="); são os parámetros 
                                            # que o método aceita
        cpf_numeric = prev_input  # Inicia a variável que conterá o CPF apenas números 
        cursor_pos = len(prev_input) # Posição inicial do cursor
        msg_start = 'Digite o CPF do cliente (ou pressione Enter para encerrar): ' # Mensagen
                                                                #inicial a ser nostrada na tela

        self.stdscr.addstr(0, 0, msg_start + ' ' * 28) # Adiciona uma string na tela (stdsrc)  
                                                    # na posição da linha 8 e coluna 8
                                                    # a string é msg start seguida por
                                                    # 28 espaços em branco
                                                    # a referida linha configura uma mensagen inicial na tela

        self.stdscr.addstr(0, len(msg_start), cpf_numeric) # Adiciona uma string (cpf_numeric)
                                                            # na tela, nas nesma linha 8 mas começando
                                                             # na coluna onde msg_start termina
                                                            # depois exibe un CPF ou valor de uma variável

        self.stdscr.refresh() # Atualiza a tela para exibir as mudanças feitas pelas chamadas 
                            # addstr anteriores.
            # O termo stdsrc geralmente se refere à "tela padrão" quando trabalhamos com a 
            # # biblioteca curses em anbientes que lidam com interfaces de usuário baseadas em texto

            # Já a biblioteca curses é usada para escrever aplicações de interface de usuario baseadas 
            # em texto e fornece uma abstração para manipular várias coisas, como a posição do cursor. 
            # cores e outras funcionalidades relacionadas ao terminal

        while True: # Inicia um loop infinito
            c = self.stdscr.getch() # Lé um caractere do teclado e armazena na variável 'c'

            if ord('\n') or c == ord('\r'): # Verifica se a tecla pressionada foi Enter 
            # (ambos '\n' e '\r' representam Enter em diferentes sistemas) 
                break # sai do Loop infinito

            elif c in (curses.KEY_BACKSPACE, 127):  # Verifica se a tecla pressionada é backspace 
                if cursor_pos > 0: # Verifica se o cursor não está na posição inicial 
                    cpf_numeric = cpf_numeric[:cursor_pos - 1] + cpf_numeric[cursor_pos:] # Remove
                                                                                            # o digito na posição atual do cursor
                    cursor_pos -= 1 # Move o cursor uma posição para a esquerda
            elif c >= ord('0') and c <= ord('9') and len(cpf_numeric) < 11: # Verifica se o
                                # caractere é um número e se já existem menos de 11 digitos 
                cpf_numeric = cpf_numeric[:cursor_pos] + chr(c) + cpf_numeric[cursor_pos:] 
                cursor_pos += 1 # Move o cursor uma posição para a direita

            # Movimentação do cursor para a esquerda
            elif c == curses.KEY_LEFT: 
                cursor_pos = max(0, cursor_pos - 1)

            elif c == curses.KEY_RIGHT: # Verifica se a tecla pressiona a seta para a direita 
                cursor_pos = min(len(cpf_numeric), cursor_pos + 1) # Move o cursor uma posição à 
                                                                # direita, sem ultrapassar o tamanho da string

            elif c == curses.KEY_DC: # Verifica se a tecla pressionada é 'Delete'
                if cursor_pos < len(cpf_numeric): # Verifica se o cursor não está no final da string
                    cpf_numeric = cpf_numeric[:cursor_pos] + cpf_numeric[cursor_pos+1:] # Remove o
                                                                   # caractere à direita do cursor.

            elif c == curses.KEY_DC: # Verifica se a tecla pressionada é 'Delete'
                if cursor_pos < len(cpf_numeric): # Verifica se o cursor não está no final da string 
                    cpf_numeric = cpf_numeric[:cursor_pos] + cpf_numeric[cursor_pos+1:] # Remove o caractere à direita do cursor

            cpf_formatted = ''.join([cpf_numeric[i:i+3] + ("." if i < 6 else '-' if i == 6 else '') for i in range(8, len(cpf_numeric), 3)]) 
            #Formata a string cpf_numeric, adicionando '.' e '-' nos lugares apropriados

            # Posição do cursor considerando os caracteres de formatação
            cursor_pos_formatted = cursor_pos + cursor_pos // 3 # Calcula a posição do cursor na string
                                                                #formatada, contando os caracteres especiais

            if cursor_pos > 6: # Verifica se o cursor está após o sexto caractere
                cursor_pos_formatted += 1 # Ajusta a posição do cursor devido ao caractere adicional '-' na formatação
            
            # Atualizando a tela
            self.stdscr.addstr(0, 0, ' ' + (len(msg_start) + 20)) # Linha a linha inicial, preenchendo-a com espaços 
            self.stdscr.addstr(0, 0, msg_start) # Exibe a mensagen iniciat na posição [8, 8]
            self.stdscr.addstr(0, len(msg_start), cpf_formatted) # Exibe o CPF formatado após a mensagen inicial 
            self.stdscr.move(0, len(msg_start) + cursor_pos_formatted - (1 if cursor_pos > 6 else 0)) # Move o cursor a para a posição correta na tela
            
            self.stdscr.refresh() # Atualiza a tela para mostrar as mudanças feitas
        return cpf_nuseric # Retorna a string cpf_numeric como resultado da função


# Erro: TypeError: App.__init__() missing 1 required positional argument: 'stdscr' 
# Tentando instanciar a classe App sem passar o parâmetro stdscr
