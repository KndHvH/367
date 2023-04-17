import os
import time
# sudo apt install sox


def main():
    small = [0.2,700] 
    large = [2,400] 
    
    while True:
        for _ in range(4):
            play_sound(small[0],small[1])
            intervalo(25,False)
                
            play_sound(small[0],small[1])
            intervalo(5)

        play_sound(large[0],large[1])
        intervalo(25)

        play_sound(large[0],large[1])






def intervalo(minutos,trabalho = True):
    for i in range(minutos):
        display_text = 'Minutos' if i!=1 else 'Minuto'
        display_text += ' para voltar ao trabalho.'if trabalho else ' para a pausa.'

        print(f'Faltam {minutos - i} {display_text}')
        time.sleep(60)


def play_sound(duration,freq):
    os.system(f'play -nq -t alsa synth {duration} sine {freq}')


if __name__ == '__main__':
   main()
