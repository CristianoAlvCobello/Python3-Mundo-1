from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hipotenusa = hypot(co,ca)

print('A hipotenusa mede {:.2f}'.format(hipotenusa))
