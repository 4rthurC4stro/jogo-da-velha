def mostrar_jogo():
    print(f' \n|{space[0]}|{space[1]}|{space[2]}|\n-------\n|{space[3]}|{space[4]}|{space[5]}|\n-------\n|{space[6]}|{space[7]}|{space[8]}|'.replace("0", " ").replace("1", "X").replace("2","O"))

def vencer(jogador):
    mostrar_jogo() 
    print(f"o jogador {jogador} venceu")
start_count = 0

jog1 = 1
jog2 = 2
space = [0,0,0,0,0,0,0,0,0]

while True:
    if space[2] == space[4] == space[6]:
        if space[4] == jog1:
            vencer(jog1)
            exit()
        elif space[4] == jog2:
            vencer(jog2)
            exit()
    if  space[0] == space[4] == space[8]:
        if space[4] == 1:
            vencer(jog1)
            exit()
        elif space[4] == 2:
            vencer(jog2)
            exit()
    if  space[0] == space[1] == space[2]:
        if space[1] == 1:
            vencer(jog1)
            exit()
        elif space[1] == 2:
            vencer(jog2)
            exit()
    if  space[3] == space[4] == space[5]:
        if space[4] == 1:
            vencer(jog1)
            exit()
        elif space[4] == 2:
            vencer(jog2)
            exit()
    if  space[6] == space[7] == space[8]:
        if space[7] == 1:
            vencer(jog1)
            exit()
        elif space[7] == 2:
            vencer(jog2)
            exit()
    if  space[0] == space[3] == space[6]:
        if space[3] == 1:
            vencer(jog1)
            exit()
        elif space[3] == 2:
            vencer(jog2)
            exit()
    if  space[1] == space[4] == space[7]:
        if space[4] == 1:
            vencer(jog1)
            exit()
        elif space[4] == 2:
            vencer(jog2)
            exit()
    if  space[2] == space[5] == space[8]:
        if space[5] == 1:
            vencer(jog1)
            exit()
        elif space[5] == 2:
            vencer(jog2)
            exit()

    if start_count % 2 == 0:
        while True:
            mostrar_jogo()
            try:
                inp_jog1 = int(input("onde vai o X?"))
                if 0>inp_jog1>9 or space[inp_jog1 - 1] == 1 or space[inp_jog1 - 1] == 2:
                    print("digito invalido, tente novamente")
                
                else:
                    space[inp_jog1 - 1] = 1
                    start_count += 1
                    break
            except:
                print("digito invalido, tente novamente")
                

    elif start_count % 2 != 0:
        while True:
            mostrar_jogo()
            try:
                inp_jog2 = int(input("onde vai o O?"))
                if 0> inp_jog2>9 or space[inp_jog2 - 1] == 1 or space[inp_jog2 - 1] == 2:
                    print("digito invalido, tente novamente")
                else:
                    space[inp_jog2 - 1] = 2
                    start_count += 1
                    break

            except:
                    print("digito invalido, tente novamente")

