import curses
import datetime
import ini

import board
import neopixel
import time

pixel_pin = board.D18

num_pixels = 96

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.45, auto_write=False, pixel_order=ORDER
)

red = 0
green = 0
blue = 0

mode = 1 # -1 - sub, 1 -  add
multiplier = 10

def quit():
    pixels.deinit()
    ini.write_config()

# tbd
#def apply_config():

def update_color(value, color):
    if (value + mode * multiplier <= 255) and (value + mode * multiplier >= 0):
        value = value + mode * multiplier
        ini.config['colors'][color] = str(value)
    return value

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(1) # set getch() non-blocking

ini.read_config()

red = int(ini.config['colors']['red'])
green = int(ini.config['colors']['green'])
blue = int(ini.config['colors']['blue'])

try:
    while 1:
        c = stdscr.getch()

        # if c != -1:
            # print(str(c) + "\n")

        if c == ord('r'):
            red = update_color(red, "red")

        if c == ord('g'):
            green = update_color(green, "green")

        if c == ord('b'):
            blue = update_color(blue, "blue")

        if c == ord('m'):
            if mode == 1:
                mode = -1
            else:
                mode = 1

        elif c == ord('q'):
            quit()
            break

        pixels.fill((red, green, blue))
        pixels.show()

        stdscr.addstr(0,0, str(red) + " " + str(green) + " " + str(blue) + "\n")
        stdscr.addstr(1,0, "Mode: " + str(mode) + "   ")

except (KeyboardInterrupt, SystemExit):
    quit()
    raise
#
finally:
    curses.endwin()
