import pygame
import mido
import board
import neopixel
from time import sleep

pixels = neopixel.NeoPixel(board.D18, 133)

pygame.init()


KEYBOARD_LEN = 61
LOWEST_NOTE_VAL = 36
HIGHEST_NOTE_VAL = 96
REF_VELOCICY = 64

LED_ARRAY_COUNT = 133
FIRST_LED = 6
LAST_LED = 128

ERROR = 0.05

RESOLUTION = ((LAST_LED - FIRST_LED)/KEYBOARD_LEN) - ERROR
STEPS = round(RESOLUTION)

#screen = pygame.display.set_mode(SIZE)
#pygame.display.set_caption("Python MIDI Program : Tarun Labs")
clock = pygame.time.Clock()
done = False
print(mido.get_input_names())
inport = mido.open_input('CASIO USB-MIDI MIDI 1')

pixels.fill((5,10,15))
sleep(2)
pixels.fill((0,0,0))
sleep(1)

try:
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        #print(event)
        for msg in inport.iter_pending():
            #print(msg)
            n = msg.note
            ref_note = round((n-LOWEST_NOTE_VAL) * RESOLUTION)+FIRST_LED
            if msg.type is 'note_on':                
                v = msg.velocity
                for i in range (STEPS):
                    pixels[ref_note+i] = (v,15,25)
            if msg.type is 'note_off':
                for i in range (STEPS):
                    pixels[ref_note+i] = (0,0,0)
            clock.tick(400)    
except AttributeError as error:
    print("Error occured!")
    pygame.quit() 
    pass
pygame.quit()    
        

