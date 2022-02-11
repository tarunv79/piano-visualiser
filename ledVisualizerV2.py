import pygame
import mido
import board
import neopixel
from time import sleep


def R(x):
    return round(x/7)
def G(x):
    return 2
def B(x):
    return 3


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

pixels = neopixel.NeoPixel(board.D18, LED_ARRAY_COUNT)
pygame.init()

RESOLUTION = ((LAST_LED - FIRST_LED)/KEYBOARD_LEN) - ERROR
STEPS = round(RESOLUTION)

#screen = pygame.display.set_mode(SIZE)
#pygame.display.set_caption("Python MIDI Program : Tarun Labs")
clock = pygame.time.Clock()
print(mido.get_input_names())
inport = mido.open_input('CASIO USB-MIDI MIDI 1')

pixels.fill((1,2,3))
sleep(1)
pixels.fill((0,0,0))
sleep(1)


def get_ref_note(n):
    if(n-LOWEST_NOTE_VAL>ERR_KEY_NUM):
        return round((n-LOWEST_NOTE_VAL) * RESOLUTION + ERR_SHIFT) + FIRST_LED
    else:
        return round((n-LOWEST_NOTE_VAL) * RESOLUTION) + FIRST_LED
    

def main_function():
    done = False
    while done == False:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            #print(event)
            for msg in inport.iter_pending():
                #print(msg)
                n = msg.note
                ref_note = get_ref_note(n)
                if msg.type is 'note_on':                
                    v = msg.velocity
                    for i in range (STEPS):
                        pixels[ref_note+i] = (R(v),G(v),B(v))
                if msg.type is 'note_off':
                    for i in range (STEPS):
                        pixels[ref_note+i] = (0,0,0)
                clock.tick(400)
        except AttributeError as error:
                print("Error occured!")
                pass

try:
    main_function()
except AttributeError as error:
    print("Error occured!")
    pygame.quit() 
    pass
pygame.quit()    
        

