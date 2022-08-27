lc_ir        = 0.11
lc_inss      = 0.08
lc_sindicato = 0.05
lc_salario_minimo = 10200


while True:
    try:
        lv_salario = float(input('Entre com o seu salario bruto: '))
        break
    except:
        print('Digite um valor valido')

if lv_salario <= lc_salario_minimo * 2:
    lc_ir = 0.00
    lc_inss = 0.08


print(f'+ Salario Bruto: R$ {lv_salario}')
print(f'- IR ({int(lc_ir*100)}%): R$ {lv_salario * lc_ir}')
print(f'- INSS ({int(lc_inss*100)}%): R$ {lv_salario * lc_inss}')
print(f'- Sindicato (5%): R$ {lv_salario * lc_sindicato}')
print(f'= Salario liquido: R$ {lv_salario - ( lv_salario * lc_ir + lv_salario * lc_inss + lv_salario * lc_sindicato) }')

