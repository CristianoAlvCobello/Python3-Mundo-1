lado1 = float(input('Digite o lado1: '))
lado2 = float(input('Digite o lado2: '))
lado3 = float(input('Digite o lado3: '))

if lado1 < lado2+lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    triangulo = str('podem')
else:
    triangulo = str('não podem')
print('os segmentos {} formar um triangulo'.format(triangulo))
