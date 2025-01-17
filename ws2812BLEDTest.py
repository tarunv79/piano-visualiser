import board
import neopixel
from time import sleep

pixels = neopixel.NeoPixel(board.D18, 1)

pixels[0] = (255,0,0)
sleep(2)
pixels[0] = (0,0,0)
sleep(2)
pixels.fill((25,25,25))


#for x in range(0,9):
   # pixels[x] = (255,50,50)
  #  sleep(1) 
    
#pixels.fill((0, 255, 0))
#sleep(3)


