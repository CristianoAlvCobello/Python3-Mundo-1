salario = float(input('Digite seu salario: '))

if salario > 1250:
    aumento = salario*0.10
    novosalario = aumento+salario
else:
    aumento = salario*0.15
    novosalario = aumento+salario

print('Seu aumento foi de R${:.2f}, seu novo salario é R${:.2f}'.format(aumento, novosalario))
