reais = float(input('Insira um valor em Reais: R$ '))

dolar = reais/3.27

print('Com R${}, você compra US${:.2f}'.format(reais, dolar))
