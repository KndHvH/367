import os
import time


# sudo apt install sox                                                                                                                         git:2*


def main():
    small = [0.2,700] 
    large = [2,400] 

    #teste
    play_sound(small[0],small[1])
    time.sleep(1)
    play_sound(small[0],small[1])
    time.sleep(1)
    play_sound(small[0],small[1])
    time.sleep(1)
    play_sound(large[0],large[1])
    
    while True:
        for _ in range(4):
            time.sleep(1500)
            play_sound(small[0],small[1])
            time.sleep(300)
            play_sound(small[0],small[1])
        play_sound(large[0],large[1])
        time.sleep(1500)
        play_sound(large[0],large[1])



        
    
    

def play_sound(duration,freq):
    os.system(f'play -nq -t alsa synth {duration} sine {freq}')


if __name__ == '__main__':
   main()
