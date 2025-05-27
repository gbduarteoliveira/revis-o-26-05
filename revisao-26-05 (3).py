# 1. Declare 3 variáveis representando nome, idade e nota de um aluno. Depois, exiba esses dados com print.
# 2. Crie expressões utilizando operadores aritméticos e relacionais.
# 3. Peça uma nota e diga se o aluno foi aprovado (nota ≥ 6).
# 4. Imprima os números de 1 a 10 usando um laço for.
# 5. Crie uma função que receba dois números e retorne a soma.
# 6. Peça ao usuário seu nome e idade e exiba em uma frase formatada.
# 7. Crie uma lista com 5 frutas e imprima a segunda e a última fruta.
# 8. Crie uma matriz 3x3 com números de 1 a 9 e imprima todos os elementos da diagonal principal.
# 9. Peça um número ao usuário e use try/except para impedir erro caso ele digite texto.
# 10. Peça para o usuário inserir uma frase e a modifique com pelo menos 3 métodos de string
# 11. Use um while para pedir um número maior que zero. Se o número for negativo, use continue para pedir de novo.
# 12. Crie um código com dois for que imprimam a tabuada de 1 a 5.
# 13. Use range para imprimir os múltiplos de 3 entre 0 e 30.
# 14. Crie uma tupla com os dias da semana e mostre a terça-feira.
# 15. Peça uma idade e use uma operação ternária para dizer se é maior de idade.
# 16. Crie uma função com dois parâmetros: nome e curso. Ela deve imprimir uma saudação.
# 17. Altere a função anterior para que, ao invés de print, ela retorne a saudação.
# 18. Crie um programa que cadastre nome, idade e curso de um aluno em um dicionário. A chave será o nome do aluno, o valor será outro dicionário com idadae e nota final. Exiba nome, idade e nota de cada aluno


# 1
# nome="yuri"
# idade= "18"
# nota=100000
# print(nome,idade,nota)

# 2
# num1=int(input("digite o 1 numero: "))
# num2=int(input("digite o 2 número: "))
# soma= (num1-num2)
# print(soma)

# 3
# nota=float(input("digite a 1 nota: "))
# if nota>=6:
#     print ("parabéns você foi aprovado")
# else:
#     print("reprovado, estude mais")
 
# 4
# for i in range(0, 10, 1):
#     i += 1
#     print(i)

# 5
# def soma(num1,num2):
#     return num1+num2
# resultado = soma(8,3)
# print(resultado)

 
# 6
# nome=str(input("digite o nome: "))
# idade=int(input("digite a idade:  "))
# print(f"meu nome é {nome}, e minha idade é {idade}")
# if nome== "yuri":
#     print("seu nome é lindo")
# else:
#     print ("seu nome é feio")

# #7 
# frutas =["melancia", "jabuticaba","manga","morango", "uvacroc"]
# print(frutas[1],frutas[-1])
 
# #8
# Matriz =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(Matriz[0][0], Matriz[1][1], Matriz[2][2])

# 9
# try:
#     num1 = int(input("Digite o 1 numero: "))
#     num2= int(input("Digite o 2: "))
#     print(num1 / num2)
# except ValueError:
#     print(" Digite apenas números.")
# 10
# texto= "olá mundo"
# print(texto.upper())
# print(texto.lower())
# print(texto.split())

# # 11
# while True:
#     i= int(input("digite um numero"))
#     if i<0:
#      continue
#     else:
#        print("sucesso")
#        break
# 12
# for i in range(1, 6): 
#     print(f"Tabuada do {i}:")
#     for b in range(1, 11):  
#         print(f"{i} x {b} = {i * b}")
           

# 13

# for i in range(0,30,3):
#     i+=3
#     print(i)

# 14

# tupla= ("segunda","terça","quarta","quinta","sexta","saábado","domingo")
# print(tupla[1])

# 15
# idade = int(input("digite sua idade: "))
# status = "Maior de idade" if idade >= 18 else "Menor de idade"
# print(status) 

# 16
# def cadastro ():
#     nome=str(input("digite o seu nome: "))
#     curso=str(input("qual o nome do seu curso? :  "))
#     print(f"Bem vindo {nome}, seu curso  é {curso}")

# cadastro()

# 17
# def cadastro():
#     nome = str(input("Digite o seu nome: "))
#     curso = str(input("Qual o nome do seu curso? : "))
    
#     return print( f"Olá, {nome}! Seja bem-vindo ao curso de {curso}.")
# cadastro()

# 18

# nome = input("Digite o nome do aluno: ")
# idade = int(input("Digite a idade do aluno: "))
# nota_final = float(input("Digite a nota final do aluno: "))

# aluno = {
#     nome: {
#         "idade": idade,
#         "nota_final": nota_final
#     }
# }

# print("=== Dados do Aluno ===")
# print(f"Nome: {nome}")
# print(f"Idade: {aluno[nome]['idade']}")
# print(f"Nota Final: {aluno[nome]['nota_final']}")

