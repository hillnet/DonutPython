#!/usr/bin/env python3

import os
import math
import numpy as np


NEWLINE = '\n'
PHI_STEP = 0.07
THETA_STEP = 0.02
DENSITY_CHARS = ".,-~:;=!*#$@"
# TWO_PI = math.pi * 2
TWO_PI = 6.28
CLEAR_CONSOLE = "\x1b[2J"


def main():

    buffer = []

    a = 0
    b = 0

    height = 80
    width = 20

    buffer_size = height * width

    outer_size = width / 40.0

    print(CLEAR_CONSOLE)
    # clear_console()

    while True:
        buffer.clear()
        buffer = [" " for i in range(buffer_size)]
        z = [0.0 for i in range(7040)]
    
        for phi in np.arange(0, TWO_PI, PHI_STEP):
            for theta in np.arange(0, TWO_PI, THETA_STEP):
                sin_theta = math.sin(theta)
                cos_theta = math.cos(theta)
                cos_phi = math.cos(phi)
                sin_phi = math.sin(phi)
                sin_a = math.sin(a)
                cos_a = math.cos(a)
                sin_b = math.sin(b)
                cos_b = math.cos(b)
                h = cos_phi + outer_size
                d = 1 / (sin_theta * h * sin_a + sin_phi * cos_a + 5)
                t = sin_theta * h * cos_a - sin_phi * sin_a
                x = int((width / 2) + 30 * d * (cos_theta * h * cos_b - t * sin_b))
                y = int((height / 2 + 1) + 15 * d * (cos_theta * h * sin_b + t * cos_b))
                o = int(x + width * y)
                n = int(8 * ((sin_phi * sin_a - sin_theta * cos_phi * cos_a) * cos_b - sin_theta * cos_phi * sin_a - sin_phi * cos_a - cos_theta * cos_phi * sin_b))

                if height > y > 0 and 0 < x < width and d > z[o]:
                    z[o] = d
                    buffer[o] = DENSITY_CHARS[n if n > 0 else 0]

        print_buffer(buffer, buffer_size, width)

        a += 0.04
        b += 0.02


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def print_buffer(buffer, buffer_size, width):
    # clear_console()
    print("\x1b[H")
    for k in range(buffer_size):
        print(buffer[k] if k % width else NEWLINE)
        # print(NEWLINE if k % width else buffer[k])


if __name__ == "__main__":
    main()
