import readchar

while True:
    tecla = readchar.readkey()
    if tecla == readchar.key.BACKSPACE:
        print('BACKSPACE')
    elif tecla == readchar.key.UP:
        print('UP')
    elif tecla == readchar.key.ENTER:
        print('ENTER')
    else:
        print(tecla)