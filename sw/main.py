from neopixel import NeoPixel
from machine import Pin

np = NeoPixel(Pin(13),1)
np[0] = (255,2,54)
np.write()

import rainbow