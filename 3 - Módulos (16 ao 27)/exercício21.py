from pygame import mixer

controle = input('Vamos ouvir Rebirth-Angra? s/n: ').strip().lower()
instrucoes = 'INSTRUÇÕES: \n Pausar = (p) \n Continuar = (c) \n Recomeçar = (r) \n Finalizar = (f) \n Alterar Volume = (v) \n Digite aqui: '

if controle == 's':
    mixer.init()
    mixer.music.load('3 - Módulos (16 ao 27)/rebirth.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.2)
    controle = input(instrucoes).strip().lower()

    while controle != 'f': 

        if controle == 'p':
            print('-=-' * 10)
            print('Musica pausada')
            print('-=-' * 10)
            mixer.music.pause()
    
        elif controle == 'c':
            print('-=-' * 10)
            print('Musica Continuando')
            print('-=-' * 10)
            mixer.music.unpause()
         
        elif controle == 'r':
            print('-=-' * 10)
            print('Musica Recomeçando')
            print('-=-' * 10)
            mixer.music.rewind()
       
        elif controle == 'v':
            volume = float(input('Digite o volume de 0 a 100: '))
            print('-=-' * 10)
            print('Volume alterado para {:.0f}%'.format(volume))
            print('-=-' * 10)
            volumemixer = volume/100
            mixer.music.set_volume(volumemixer)

        controle = input(instrucoes).strip().lower()

    else:
            print('-=-' * 10)
            print('Obrigado por ouvir')
            print('-=-' * 10)
    