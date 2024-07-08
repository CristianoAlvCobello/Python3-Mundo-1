distancia = float(input('Digite uma distância: '))

km = distancia/1000
hm = distancia/100
dam = distancia/10
m = distancia
dm = distancia*10
cm = distancia*100
mm = distancia*1000

print('{} Km'.format(km))
print('{} Hm'.format(hm))
print('{} Dam'.format(dam))
print('{} M'.format(m))
print('{} Dm'.format(dm))
print('{} Cm'.format(cm))
print('{} mm'.format(mm))
