dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))

valoraluguel = dias*60
valorkm = km*0.15
valorfinal = valoraluguel+valorkm

print('Valor dos dias: R${:.2f}'.format(valoraluguel))
print('Valor dos Km: R${:.2f}'.format(valorkm))
print('Valor total R${:.2f}'.format(valorfinal))
