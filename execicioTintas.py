from ast import If
from functools import total_ordering
from math import ceil, floor
from turtle import clear   

def calculoTinta(metro_quadrado):
    litro_usado = float(metro_quadrado) / 6
    total_lata  = litro_usado * 1.1  / 18
    total_lata  = ceil(total_lata)
    total_galao =  litro_usado / 3.6
    total_galao =  ceil(total_galao)
    total_preco_lata = total_lata * 80
    total_preco_galao = total_galao * 25
    return total_lata, total_preco_lata, total_galao, total_preco_galao

def consumoOtimizado(metro_quadrado):
    litro_usado       = float(metro_quadrado) / 6
    total_galao       = 0
    total_lata        = 0
    total_preco_galao = 0
    total_preco_lata  = 0
    if litro_usado > 18:
        sobra = litro_usado % 18
        total_lata = litro_usado / 18
        total_lata = floor(total_lata)
        total_preco_lata = total_lata * 80
        if sobra >= 3.6:
            total_galao = sobra / 3.6
            total_galao = ceil(total_galao)
            total_preco_galao = total_galao * 25
        else:
            total_galao = 1
            total_preco_galao = total_galao * 25
    elif (18 - litro_usado) < (litro_usado % 3.6):
        total_lata = 1
        sobra = 18 - litro_usado
        total_preco_lata = total_lata * 80
    else:

        sobra = litro_usado % 3.6
        total_galao = litro_usado / 3.6
        total_galao = ceil(total_galao)
        total_preco_galao = total_galao * 25

    return total_lata, total_preco_lata, total_galao, total_preco_galao 




metro_quadrado = input("Informe o tamanho em m² a ser píntada:")
"""
total_lata, total_preco_lata, total_galao, total_preco_galao = calculoTinta(metro_quadrado)

print(f'Quantidade total de latas: {total_lata} \nValor total: R${total_preco_lata}')
print(f'Quantidade total de galao: {total_galao} \nValor total: R${total_preco_galao}')
"""
print("Calculo otimizado")
"""
clear(total_lata, total_preco_lata, total_galao, total_preco_galao)
"""
total_lata, total_preco_lata, total_galao, total_preco_galao = consumoOtimizado(metro_quadrado)

print(f'Quantidade total de latas: {total_lata} \nValor total: R${total_preco_lata}')
print(f'Quantidade total de galao: {total_galao} \nValor total: R${total_preco_galao}')
print(f'Valor total R$ {total_preco_galao + total_preco_lata}')









