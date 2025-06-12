 # ## Atividades de Revisão - Lógica de Programação

# ### 1. Variáveis e Tipos de Dados
# 1. Declare três variáveis: nome (string), idade (inteiro) e altura (float).
# idade = 18
# nome = "Yuri"
# altura = 1.68
# print(f'você tem {idade} anos, seu nome é {nome}, e sua altura é {altura}')

# 2. Receba do usuário dois números e mostre a soma.
# num1=int(input("digite um número"))
# num2= int(input("digite o segundo número"))
# soma=num1+num2
# print(soma)
# 3. Receba o nome de uma pessoa e exiba "Olá, \[nome]!".
# nome =str(input("digite seu nome"))
# print(f'olá {nome}')


# 4. Escreva um programa que calcule a área de um retângulo (base \* altura).
# base = int(input("Digite a base do retângulo: "))
# altura = int(input("Digite a altura do retângulo: "))
# area = (base*altura)
# print(f"A área do retângulo é {area}")



# ### 2. Operadores Aritméticos e Relacionais

# 5. Receba dois números e exiba a média entre eles.
# num1 =int(input("Digite um número: "))
# num2 =int(input("Digite outro número: "))
# media = ((num1+num2)/2)
# print(media)

# 6. Verifique se um número é par ou ímpar.
# num =int(input("Digite um número: "))
# if num%2==0:
#  print("esse número é par")
# else:
#  print("esse número é impar")

# 7. Peça ao usuário um número e diga se ele é maior que 100.
# num1=int(input("digite um número: "))
# if num1>100:
#     print("esse número é maior que 100")
# else:
#     print("esse número é menor que 100")

# 8. Receba dois valores e diga qual é o maior.
# num1=float(input("digite um número"))
# num2=float(input("digite um número"))
# if num1>num2:
#     print(f"o {num1} é o maior")
# else:
#     print(f"o {num2} é o maior")

# ### 3. Cndicionais (if/else)

# 9. Crie um programa que receba a idade e diga se é maior de idade.
# idade=int(input("digite a sua idade"))
# if idade>=18:
#     print("você é maior de idade")
# else:
#     print("você é menor de idade")

# 10. Crie um sistema simples de login com usuário e senha fixos.
# Usuário e senha fixos
# login_correto = "yurilindo"
# senha_correta = "yurimuitobonito"
# while True:
#     login = input("Digite o login: ")
#     senha = input("Digite a senha: ")

#     if login == login_correto and senha == senha_correta:
#         print("Login bem-sucedido! Bem-vindo,", login)
#         break
#     else:
#         print("Login ou senha incorretos. Tente novamente.")




# 11. Calcule a média de três notas e informe se o aluno foi aprovado (nota ≥ 6).
# num1 =int(input("Digite um número: "))
# num2 =int(input("Digite outro número: "))
# num3 =int(input("Digite outro número: "))
# media = ((num1+num2+num3)/3)
# if media>=6:
#  print("aprovado")
# else:
#  print("reprovado")



# 12. Receba o nome de um produto e o valor. Aplique um desconto se o valor for maior que R\$ 100.
# nome = input("Digite o nome do produto: ")
# valor = float(input("Digite o valor: "))
# desconto = valor * 0.50

# if valor > 100:
#     valor_com_desconto = valor - desconto
#     print("Esse é o valor com o desconto:", valor_com_desconto)
# else:
#     print("O valor do produto é:", valor)


# ### 4. Laços de Repetição (while/for)

# 13. Imprima os números de 1 a 10 com `while`.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# 14. Faça a tabuada de um número com `for`.
# for i in range(2): 
#     print(f"Tabuada do {i}:")
#     for b in range(1, 11):  
#         print(f"{i} x {b} = {i * b}")

# 15. Receba números até que o usuário digite 0, e some todos os valores.
# soma = 0
# while True:
#     numero = int(input("Digite um número (0 para sair): "))
#     if numero == 0:
#         break
#     soma += numero

# print("A soma dos números digitados é:", soma)

# 16. Conte de 1 até 100 e mostre apenas os múltiplos de 5.
# for i in range(-1, 100, 5):
#     i += 1
#     print(i)

# ### 5. Funções

# 17. Crie uma função que receba um nome e diga "Bom dia, \[nome]".
# def saudacao():
#     nome = input("Digite seu nome: ")
#     print(f"Bom dia, {nome}!")
# saudacao()

# 18. Faça uma função que receba dois números e retorne o maior.
# def maior_numero():
#     num = int(input("Digite um número: "))
#     num2 = int(input("Digite outro número: "))
    
#     if num > num2:
#         return num
#     else:
#         return num2

# maior = maior_numero()
# print(f"O maior número é: {maior}")

# 19. Crie uma função que calcule o fatorial de um número.

# def fatorial():
#     num = int(input("Digite um número: "))
#     resultado = 1
#     for i in range(1, num + 1):
#         resultado *= i
#     print(f"O fatorial de {num} é {resultado}")
# fatorial()

# 20. Faça uma função que diga se um número é primo.
# def eh_primo(n):
#     if n <= 1:
#         return False  
#     for i in range(2, int(n**0.5) + 1): 
#         if n % i == 0:
#             return False  
#     return True  
# num = int(input("Digite um número: "))
# if eh_primo(num):
#     print(f"{num} é primo!")
# else:
#     print(f"{num} não é primo.")


# ### 6. Input/Output e Strings

# 21. Receba uma frase e diga quantas palavras ela tem.
# frase = input("Digite uma frase: ")
# palavras=frase.split()
# quantidade = len(palavras)  
# print(f"A frase tem {quantidade} palavras.")


# 22. Leia uma string e imprima cada letra em uma linha.

# frase=str(input("digite uma frase"))
# for letra in frase:
#     if letra != " ":  
#         print(letra)


# 23. Verifique se uma palavra é um palíndromo (ex: "arara").
# palavra=input("digite a palavra")
# if palavra [0]== palavra [-1]:

#     print("é um palindromo")
# else:
#     print("essa palavra não é um palindromo")
    
# 24. Transforme uma string em maiúsculas sem usar `.upper()`.

# frase =  "olá mundo" 
# frase_maiuscula=  frase . capitalize () 
# print ( frase_maiuscula )

# ### 7. Listas

# # 25. Crie uma lista com 5 nomes e imprima todos.
# nomes= ["Gabriel", "Yuri", "Bebel"]
# for nome in nomes:
#     print(nome)

# 26. Peça 5 números ao usuário e guarde em uma lista.
# numeros=[]
# for i in range(5):
#     numero= int(input("digite o numero"))
#     numeros.append(numero)
# print(numeros)

# 27. Some os elementos de uma lista de números.
# numeros=[1,2,3,4,5]
# soma= sum(numeros)
# print(soma)

# 28. Encontre o maior e o menor número de uma lista.
# numeros=[1,2,3,4,5]
# print("max:", max(numeros))
# print("min:", min(numeros))

# ### 8. Matrizes

# 29. Crie uma matriz 3x3 e preencha com valores do usuário.
#matriz = []

#for i in range(3):
 #   linha = []
 #  for j in range(3):
#        valor = int(input("Digite um número: "))
#       linha.append(valor)
 #   matriz.append(linha)

#print("Matriz 3x3:")
#print(matriz)
#30. Some todos os elementos da matriz.
# Matriz = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
# ]
# soma = sum(sum(linha) for linha in Matriz)
# print(soma)


# 31. Mostre os elementos da diagonal principal.

# Matriz =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(Matriz[0][0], Matriz[1][1], Matriz[2][2])

# # 32. Encontre o maior valor de cada linha.
# Matriz =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for linha in Matriz:
#     print (max(linha))



# ### 9. Try e Except

# 33. Faça um programa que peça um número e trate erro se o usuário digitar letra.
# try:
#     numero=int(input("digite um número: "))
# except ValueError:
#     print(" Digite apenas números.")


# 34. Crie uma calculadora que continue funcionando mesmo com divisões por zero (exiba mensagem de erro).

# try:
#     x = int(input("Digite o numerador: "))
#     y = int(input("Digite o denominador: "))
#     print(x / y)
# except ValueError:
#     print(" Digite apenas números.")
# except ZeroDivisionError:
#     print(" Divisão por zero não é permitida.")


# 35. Peça a idade e trate erros de valor inválido (ex: texto em vez de número).
# try:
#  idade=int(input("digite sua idade: "))
# except ValueError:
#    print(" Digite apenas números: ")

# ### 10. Métodos de String

# 36. Receba um nome e transforme em letras minúsculas.
# texto=str(input("digite seu nome: "))
# print(texto.lower())

# 37. Peça uma frase e conte quantas vezes aparece a letra “a”.
# texto=str(input("digite seu nome: "))
# print(texto.count("a"))

# # 38. Verifique se uma string começa com “A”.
# texto=str(input("digite seu nome: "))
# if texto.startswith ("a"):
#     print("essa palavra começa com a")
# else :
#     print("essa palavra não começa com a")
# ### 11. While + Continue

# 39. Conte de 1 a 10, pulando os múltiplos de 3.

# i=1
# while i<=10:
#     if i % 3==0:
#         i+=1
#         continue
#     print(i)
#     i+=1
    

# 40. Peça 10 números e ignore os negativos com `continue`.
# i=0
# while i<10:
#     numero=int(input("digite um numero: "))
#     if numero>0:
#         continue
#     i+=1
    
# for i in range(10):
#     numero=int(input("digite um numero"))
#     if numero<0:
#         continue
    

# ### 12. Laços Internos (Loop dentro de Loop)

# 41. Imprima uma tabela de multiplicação (1 a 10) com `for` aninhado.
# for numero in range(1, 11):
#     resultado = 10 * numero
#     print(f"10 x {numero} = {resultado}")

# 42. Preencha uma matriz 3x3 com `for` duplo.
# Matriz = []
# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f"Digite o valor para [{i}][{j}]: "))
#         linha.append(valor)
#     Matriz.append(linha)  
# print("Matriz final:")
# for linha in Matriz:
#     print(linha)

# ### 13. For + Range

# 43. Use `range` para mostrar os números pares de 2 a 20.
# for i in range(2,21,2):
#     print(i)

# 44. Crie um `for` que mostre os números de 10 a 1 (decrescente).
# for i in range(10,0,-1):
#     print(i)


# ### 14. Tuplas

# 45. Crie uma tupla com os dias da semana e mostre o terceiro dia.
# semana=("segunda","terça","quarta", "quinta","sexta","sabado","domingo");
# print(semana[2])


# 46. Verifique se um valor está presente em uma tupla.
# semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo")
# dia = str(input("digite algum dia da semana"))
# if dia in semana:
#     print(f"O dia '{dia}' está na tupla.")
# else:
#     print(f"O dia '{dia}' não está na tupla.")


# 47. Crie uma tupla com nomes e mostre seu tamanho.
# nomes = ("Yuri", "Gabriel", "Isabela", "joão", "felipe", "cesar", "cauã")
# print(len(nomes))

# ### 15. Operação Ternária

# # 48. Receba a nota e imprima "Aprovado" se for maior ou igual a 6, senão "Reprovado" (use ternário).
# nota= int(input("Digite sua nota aqui: "))
# print(f'Aprovado') if nota >=6 else print('Reprovado')

# # 49. Determine se um número é par ou ímpar com ternário.
# num= int(input("Digite um numero aqui: "))
# print(f'Par') if num %2==0 else print('Ímpar')


# ### 16. Argumentos de Funções

# 50. Crie uma função com parâmetros opcionais.
# def saudacao(nome="yuri lindo"):
#     print("oi", nome)
# saudacao()

# 51. Faça uma função que aceite um número indeterminado de argumentos.
# def mostrar_idade(*args):
#    for idades in args:
#       print(idades)
# mostrar_idade(18,20,22,23)
# ### 17. Return

# 52. Faça uma função que calcule o quadrado de um número e retorne o resultado.
# def ao_quadrado():
#     numero=int(input("digite um número: "))
#     return numero*numero
# print(ao_quadrado())



# 53. Crie uma função que receba 3 notas e retorne a média.

# def media():

#     nota1=int(input("digite a primeira nota"))
#     nota2=int(input("digite a segunda nota"))
#     nota3=int(input("digite a terceira nota"))
#     return (nota1+nota2+nota3)/3
# print(media())

    

# ### 18. Dicionários

# 54. Crie um dicionário com nome, idade e cidade de uma pessoa.
# dados={
#    "nome":"yuri", "idade":18, "cidade": "California"
# }
# print(dados)
# 55. Adicione uma nova chave chamada “email”.

# dados={
#    "nome":"yuri", "idade":18, "cidade": "California"
# }
# dados["email"]= "yurilindo@gmail.com"
# print(dados)

# 56. Faça uma função que receba um dicionário de aluno e retorne uma frase com os dados.
# def descrever_aluno(aluno):
#     nome = aluno['nome']
#     idade = aluno['idade']
#     curso = aluno['curso']
    
#     return f"O aluno {nome} tem {idade} anos e está matriculado no curso de {curso}."
# dados_do_aluno = {
#     'nome': 'Yuri Duarte',
#     'idade': 18,
#     'curso': 'ads'
# }

# frase = descrever_aluno(dados_do_aluno)
# print(frase)



# ### 19. Atividade Final Integrada

# 57. Crie um sistema simples de boletim:

# * O usuário insere o nome de 3 alunos.
# * Para cada um, insere 3 notas.
# * Calcule a média e mostre os aprovados.

# alunos = {}

# for i in range(3):
#     nome = input(f"Digite o nome do {i+1}° aluno: ")
#     notas = []
#     for b in range(3):
#         nota = int(input(f"Digite a nota {b+1} do aluno {nome}: "))
#         notas.append(nota)
    
#     media = sum(notas) / 3
#     alunos[nome] = media

#     if media >= 6:
#         print(f"{nome} foi aprovado com média {media:.1f}")
#     else:
#         print(f"{nome} foi reprovado com média {media:.1f}")
