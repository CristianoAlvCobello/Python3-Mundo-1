distancia = float(input('Qual distancia da viagem em Km? '))

if distancia > 200:
    valor = distancia*0.45
else:
    valor = distancia*0.5
print('Valor da viagem R${}'.format(valor))
