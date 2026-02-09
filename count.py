import os
def limpar():
    os.system('cls')
limpar()
n1 = int(input("digite seu numero"))
for i in range (0,11,1):
    vezes = i * n1
    print(f"{n1} X {i} = {vezes}")