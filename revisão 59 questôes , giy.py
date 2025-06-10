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

# ### 5. Funções

# 17. Crie uma função que receba um nome e diga "Bom dia, \[nome]".
# 18. Faça uma função que receba dois números e retorne o maior.
# 19. Crie uma função que calcule o fatorial de um número.
# 20. Faça uma função que diga se um número é primo.

# ### 6. Input/Output e Strings

# 21. Receba uma frase e diga quantas palavras ela tem.
# 22. Leia uma string e imprima cada letra em uma linha.
# 23. Verifique se uma palavra é um palíndromo (ex: "arara").
# 24. Transforme uma string em maiúsculas sem usar `.upper()`.

# ### 7. Listas

# 25. Crie uma lista com 5 nomes e imprima todos.
# 26. Peça 5 números ao usuário e guarde em uma lista.
# 27. Some os elementos de uma lista de números.
# 28. Encontre o maior e o menor número de uma lista.

# ### 8. Matrizes

# 29. Crie uma matriz 3x3 e preencha com valores do usuário.
# 30. Some todos os elementos da matriz.
# 31. Mostre os elementos da diagonal principal.
# 32. Encontre o maior valor de cada linha.

# ### 9. Try e Except

# 33. Faça um programa que peça um número e trate erro se o usuário digitar letra.
# 34. Crie uma calculadora que continue funcionando mesmo com divisões por zero (exiba mensagem de erro).
# 35. Peça a idade e trate erros de valor inválido (ex: texto em vez de número).

# ### 10. Métodos de String

# 36. Receba um nome e transforme em letras minúsculas.
# 37. Peça uma frase e conte quantas vezes aparece a letra “a”.
# 38. Verifique se uma string começa com “A”.

# ### 11. While + Continue

# 39. Conte de 1 a 10, pulando os múltiplos de 3.
# 40. Peça 10 números e ignore os negativos com `continue`.

# ### 12. Laços Internos (Loop dentro de Loop)

# 41. Imprima uma tabela de multiplicação (1 a 10) com `for` aninhado.
# 42. Preencha uma matriz 3x3 com `for` duplo.

# ### 13. For + Range

# 43. Use `range` para mostrar os números pares de 2 a 20.
# 44. Crie um `for` que mostre os números de 10 a 1 (decrescente).

# ### 14. Tuplas

# 45. Crie uma tupla com os dias da semana e mostre o terceiro dia.
# 46. Verifique se um valor está presente em uma tupla.
# 47. Crie uma tupla com nomes e mostre seu tamanho.

# ### 15. Operação Ternária

# 48. Receba a nota e imprima "Aprovado" se for maior ou igual a 6, senão "Reprovado" (use ternário).
# 49. Determine se um número é par ou ímpar com ternário.

# ### 16. Argumentos de Funções

# 50. Crie uma função com parâmetros opcionais.
# 51. Faça uma função que aceite um número indeterminado de argumentos.

# ### 17. Return

# 52. Faça uma função que calcule o quadrado de um número e retorne o resultado.
# 53. Crie uma função que receba 3 notas e retorne a média.

# ### 18. Dicionários

# 54. Crie um dicionário com nome, idade e cidade de uma pessoa.
# 55. Adicione uma nova chave chamada “email”.
# 56. Faça uma função que receba um dicionário de aluno e retorne uma frase com os dados.

# ### 19. Atividade Final Integrada

# 57. Crie um sistema simples de boletim:

# * O usuário insere o nome de 3 alunos.
# * Para cada um, insere 3 notas.
# * Calcule a média e mostre os aprovados.