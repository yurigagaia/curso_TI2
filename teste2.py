import os
def limpar():
    os.system("cls")
limpar()
n1 = int(input("digite seu numero"))
for i in range (0,11,1):
    vezes = n1 * i
    print(f"{n1} * {i} = {vezes}")