from pygame import mixer
mixer.init()
mixer.music.load('exercicios021.mp3')
mixer.music.play()
q = int(input("foi trollado(a)? (se sim digite {1} se não digite {0}"))
if q == 1:
    mixer.music.pause()
f = str(input('deseja continuar?'))
if f == str('sim'):
    mixer.music.play()