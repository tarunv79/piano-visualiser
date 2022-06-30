import pygame
import mido
import board
import neopixel
from time import sleep


def R(x):
    return 20
def G(x):
    return 20
def B(x):
    return 10


KEYBOARD_LEN = 61
LOWEST_NOTE_VAL = 36
HIGHEST_NOTE_VAL = 96
REF_VELOCICY = 64

LED_ARRAY_COUNT = 133
FIRST_LED = 6
LAST_LED = 125

#general error in calibration
ERROR = 0
#starting from key num = 1
ERR_KEY_NUM = 35
#right shift in LED length
ERR_SHIFT = -0.2

    
def flashLed():
    for i in range(5):
        pixels.fill((5,0,0))
        sleep(0.1)
        pixels.fill((0,0,0))
        sleep(0.1)

try:
    pixels = neopixel.NeoPixel(board.D18, LED_ARRAY_COUNT)
    pygame.init()    
    RESOLUTION = ((LAST_LED - FIRST_LED)/KEYBOARD_LEN) - ERROR
    STEPS = round(RESOLUTION)
    pixels.fill((1,2,3))
    sleep(1)
    pixels.fill((0,0,0))
    sleep(1)
except:
    print("INIT_ERR")
    flashLed()
    exit(1)

try:
    clock = pygame.time.Clock()
    print(mido.get_input_names())
    inport = mido.open_input('CASIO USB-MIDI MIDI 1')
except:
    print("KEYBOARD_ERR")
    flashLed()
    exit(1)

def get_ref_note(n):
    if(n-LOWEST_NOTE_VAL>ERR_KEY_NUM):
        return round((n-LOWEST_NOTE_VAL) * RESOLUTION + ERR_SHIFT) + FIRST_LED
    else:
        return round((n-LOWEST_NOTE_VAL) * RESOLUTION) + FIRST_LED

    
def main_function():
    n1=0
    n2=0
    n3=0
    done = False
    while done == False:
        try:
            for event in pygame.event.get():
                #print(event)
                #print(event.type)
                if event.type == pygame.QUIT:
                    done = True
            for msg in inport.iter_pending():
                #print(msg)
                if msg.type is 'note_on' or msg.type is 'note_off':
                    n = msg.note
                    ref_note = get_ref_note(n)
                    if msg.type is 'note_on':
                        v = msg.velocity
                        for i in range (STEPS):
                            pixels[ref_note+i] = (R(v),G(v),B(v))
                        if n is LOWEST_NOTE_VAL:
                            n1 = LOWEST_NOTE_VAL
                        elif n is HIGHEST_NOTE_VAL:
                            n2 = HIGHEST_NOTE_VAL
                        elif n is LOWEST_NOTE_VAL+1:
                            n3 = LOWEST_NOTE_VAL +1
                    if msg.type is 'note_off':
                        for i in range (STEPS):
                            pixels[ref_note+i] = (0,0,0)
                    clock.tick(400)
          
            if n1 is LOWEST_NOTE_VAL and n2 is HIGHEST_NOTE_VAL and n3 is LOWEST_NOTE_VAL+1:
                 pygame.quit()
                 print("Exiting the program...")
                 pixels.fill((1,3,2))
                 sleep(1)
                 pixels.fill((0,0,0))
                 break
            else:
                    n1=0
                    n2=0
                    n3=0
        except AttributeError as error:
                pass

try:
    print("Starting the main program...")
    main_function()
except:
    print("EXEC_ERR")
    flashLed()
    pygame.quit() 
    exit(1)
pygame.quit()
print("Bye!")
        


