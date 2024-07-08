salario = float(input('Digite o salário: '))
aumento = float(input('Porcento de aumento: '))

aumento = aumento/100
salarioaumento = salario+(salario*aumento)

print('Salário sem aumento: R${:.2f}'.format(salario))
print('Salário com aumento: R${:.2f}'.format(salarioaumento))
