def calcular_desconto(valor_total, desconto):
    desconto_total = valor_total * float(desconto)
    valor_final = valor_total - desconto_total
    return valor_final

valor_com_desconto = calcular_desconto(1000, 0.1)
print(f'Valor da compra com desconto R${valor_com_desconto:.2f}')