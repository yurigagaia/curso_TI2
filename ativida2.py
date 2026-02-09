#Não apague todo o código. Corrija apenas o que for necessário. 
#Exercício 1 – Debugando lista de nomes 
#O código abaixo deveria adicionar nomes a uma lista e depois mostrar todos, mas não funciona corretamente. 
 
nomes = [] 
 
def adicionar_nome(): 
    nome = input("Digite um nome: ") 
    nomes.append(nome) 
 
def listar_nomes(): 
    for nome in nomes: 
        print(nome) 
 
adicionar_nome() 
listar_nomes() 
 
#Exercício 2 – Debugando calculadora simples 
#O código abaixo deveria somar dois números digitados pelo usuário, mas o resultado está errado. 
 
def somar(a, b): 
    return a + b 
 
a = float(input("Digite o primeiro número: ")) 
b = float(input("Digite o segundo número: ")) 
 
resultado = somar(a, b) 
print("Resultado:", resultado) 
 
#Exercício 3 – Debugando cadastro de notas 
#O código abaixo deveria calcular a média das notas digitadas, mas apresenta um erro. 
 
notas = [] 
 
def adicionar_nota(): 
    nota = float(input("Digite a nota: ")) 
    notas.append(nota) 
 
def calcular_media(): 
    media = sum(notas) / len(notas) 
    print("Média:", media) 
 
adicionar_nota() 
adicionar_nota() 
calcular_media() 
 
#Exercício 4 – Debugando impressão de números 
#O código abaixo deveria mostrar o número digitado, mas apresenta um erro ao executar. 
 
numeros = [] 
 
def adicionar_numero(): 
    numero = int(input("Digite um número: ")) 
    numeros.append(numero) 
 
def listar_numeros(): 
    print(numeros[0]) 
 
adicionar_numero() 
listar_numeros() 
 
#Exercício 5 – Debugando soma simples 
#O código abaixo deveria calcular a soma de dois números, mas o programa não funciona. 
 
def somar():
    a = int(input("digite um nome"))
    b = int(input("digite o segundo numero")) 
    resultado = a + b 
    print("Resultado:", resultado) 
 
somar() 