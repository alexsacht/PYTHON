"""
1- Crie uma função que exibe uma saudação com os parametros saudação e nome.
"""

def saudacao(msg, nome):
    print(f'{msg} {nome}')

print()
print('Exercicio 1: ')
saudacao("Ola", "Alex")
print('-----------------------------------')
print()

"""
2- Crie uma função que recebe 3 numeros como parametros e exiba a soma entre eles.
"""

def soma(num1, num2, num3):
        return num1 + num2 + num3
    
soma = soma(1.1,2,3)

print('Exercicio 2: ')
print(f'{soma}')
print('-----------------------------------')
print()


"""
3- Crie uma função que recebça 2 numeros. O primeiro é um valor e o segundo um percentual (ex. 10%).
Returne o valor do primeiro numero somado do aumento do percentual do mesmo.
"""

def porcentagem(num1, percentual):
    num1 = num1 + num1 * percentual / 100
    return num1

valor = porcentagem(100,50)

print('Exercicio 3: ')
print(f' {valor}')
print('-----------------------------------')
print()


"""
4- Fizz Buss - Se o parametro da função for divisivel por 3 retorne fizz, se o parametro da função for divisivel
poir 5, retorne buss. Se o parametro da função for divisivel por 5 e por 3, retorne FizzBuzz
caso contrario, retorne o numero enviado
"""

def fizzbuss(num1):
    if num1 % 3 == 0:
        if num1 % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    elif num1 % 5 == 0:
        return 'Buzz'
    else:
        return num1

var1 = fizzbuss(15)

print('Exercicio 4: ')
print(var1)
print('-----------------------------------')
print()