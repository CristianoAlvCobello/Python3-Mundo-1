from datetime import date
ano = int(input('Qual ano quer analisar? digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} É um ano bissexto'.format(ano))
else:
    print('{} É um ano normal'.format(ano))
