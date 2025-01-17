import board
import neopixel
from time import sleep

LED_ARRAY_COUNT = 133


pixels = neopixel.NeoPixel(board.D18, LED_ARRAY_COUNT)

for i in range(2):
    pixels.fill((0,5,0))
    sleep(0.5)
    pixels.fill((0,0,0))
    sleep(0.5)
    


