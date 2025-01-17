import pygame
import mido

pygame.init()

BLACK = [0,0,0]
WHITE = [150,10,225]

note_list = []
note_list_off = []


KEYBOARD_LEN = 61
LOWEST_NOTE_VAL = 36
HIGHEST_NOTE_VAL = 96
REF_VELOCICY = 64

notes = []

SIZE = [1024,480]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Python MIDI Program : Tarun Labs")
clock = pygame.time.Clock()
done = False

for i in range(KEYBOARD_LEN):
    notes.insert(i,0)

print(mido.get_input_names())
inport = mido.open_input('CASIO USB-MIDI MIDI 1')

try:
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        #print(event)
        for msg in inport.iter_pending():
            #print(msg)
            if msg.type is 'note_on' or msg.type is 'note_off':
                n = msg.note
                notes[n-LOWEST_NOTE_VAL] = msg.velocity
                x=n*10
                if msg.velocity>REF_VELOCICY:
                    note_list.append([x,0])
                else:
                    note_list_off.append([x,0])
        pygame.display.flip()
    
        for i in range(len(note_list)):
            pygame.draw.circle(screen, WHITE, note_list[i], 10)
            note_list[i][1] += 1
        
    
        for i in range(len(note_list_off)):
            pygame.draw.circle(screen, BLACK, note_list_off[i], 10)
            note_list_off[i][1] += 1
        
        print(notes)    
        clock.tick(400)
except AttributeError as error:
    print("Error occured!")
    pygame.quit() 
    pass
pygame.quit()    
        
