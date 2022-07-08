nome = input('Digite o nome do aluno: ')
print('')
print('digite SAIR para finalizar')
print('')
total = 0
nota = 0
soma = 0
while True:
    nota = input('Digite a nota: ')
    if nota.isdigit():
        total += 1.
        soma = soma + int(nota)
    elif nota == 'SAIR':
        break

if total == 0:
    print('nenhuma nota digitada')
    exit()

if soma / total >= 7:
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'

print(f'O aluno {nome} teve umá media de {soma / total} com isso ele foi {resultado} !!' )




