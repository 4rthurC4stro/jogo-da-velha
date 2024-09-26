def mostrar_jogo():
    print(f' \n|{space[0]}|{space[1]}|{space[2]}|\n-------\n|{space[3]}|{space[4]}|{space[5]}|\n-------\n|{space[6]}|{space[7]}|{space[8]}|'.replace("0", " ").replace("1", "X").replace("2","O"))

def vencer(jogador):
    mostrar_jogo() 
    print(f"o jogador {jogador} venceu")
    exit()


def verify_win():
    combinations =[
                (0,1,2),(3,4,5),(6,7,8),
                (0,4,8),(2,4,6),(0,3,6),
                (1,4,7),(2,5,8)
                ]
    for a,b,c in combinations:
        if space[a] == space[b] == space[c] and space[a] != 0:
            vencer(space[a])
def verify_tie():
    
    return all([pos != 0 for pos in space]) 
start_count = 0

jog1 = 1
jog2 = 2
space = [0] * 9





while True:
    

    if start_count % 2 == 0:
        while True:
            mostrar_jogo()
            try:
                inp_jog1 = int(input("onde vai o X?"))
                if 0>inp_jog1>9 or space[inp_jog1 - 1] == 1 or space[inp_jog1 - 1] == 2:
                    print("digito invalido, tente novamente")
             
                else:
                    space[inp_jog1 - 1] = 1
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
                    break

            except:
                    print("digito invalido, tente novamente")
    verify_win()
    if verify_tie():
        mostrar_jogo()
        print("o jogo deu empate")
        exit()
    start_count += 1
