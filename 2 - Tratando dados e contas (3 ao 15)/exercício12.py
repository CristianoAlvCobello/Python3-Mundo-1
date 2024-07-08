valor = float(input('Digite o valor: '))
promocao = float(input('Porcento de desconto: '))

promocao = promocao/100
valor = valor-(valor*promocao)

print('Valor final R${:.2f}'.format(valor))
