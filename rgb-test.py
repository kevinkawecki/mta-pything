#!/usr/bin/env python
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)
                               + '/../bindings/python/'))
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options = options)

offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("../fonts/6x13.bdf")
textColor = graphics.Color(255, 255, 0)
pos = offscreen_canvas.width
my_text = "Hi Alex"


try:
    print("Press CTRL-C to stop.")
    while True:
        offscreen_canvas.Clear()

        red = graphics.Color(255, 0, 0)
        graphics.DrawLine(offscreen_canvas, 5, 5, 22, 13, red)
        #len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
        len = graphics.DrawText(offscreen_canvas, font, 0, 10, textColor, my_text)
        len = graphics.DrawText(offscreen_canvas, font, 0, 24, textColor, "from kevin")
        #pos -= 1
        #if (pos + len < 0):
        #    pos = offscreen_canvas.width

        #print(f"POS: {pos}")

        #time.sleep(0.05)
        time.sleep(1)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
except KeyboardInterrupt:
    sys.exit(0)
