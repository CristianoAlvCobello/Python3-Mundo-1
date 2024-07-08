numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
numero3 = int(input('Digite o número 3: '))

#Verificação do maior
if numero1 > numero2 and numero1 >numero3:
    maior = numero1

if numero2 > numero1 and numero2 > numero3:
    maior = numero2

if numero3 > numero1 and numero3 > numero2:
    maior = numero3

#Verificação do menor
if numero1 < numero2 and numero1 < numero3:
    menor = numero1

if numero2 < numero1 and numero2 < numero3:
    menor = numero2

if numero3 < numero1 and numero3 < numero2:
    menor = numero3

print('O maior número foi: {}'.format(maior))
print('O menor número foi: {}'.format(menor))
