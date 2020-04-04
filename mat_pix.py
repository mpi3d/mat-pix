# !/usr/bin python3.7
# -*- coding: utf-8 -*-

from os.path import isfile
from time import sleep
from random import randint
from argparse import ArgumentParser
from json import load, dump
from board import D18
from neopixel import NeoPixel

GPIO = D18
LED_NUM = 8

class MatPix:
    def __init__(self):
        parser = ArgumentParser()
        action = parser.add_mutually_exclusive_group()
        parser.add_argument("-b", "--brightness", help="set the brightness",
                            metavar="BRIGHTNESS", default=100, type=int)
        action.add_argument("-c", "--clear", help="clear all leds", action="store_true")
        action.add_argument("-g", "--get", help="get color of a led",
                            metavar="LEDID", type=int)
        action.add_argument("-s", "--set", help="set color of a led",
                            metavar=("LEDID", "RED", "GREEN", "BLUE"), type=int, nargs=4)
        action.add_argument("-S", "--setall", help="set color of all leds",
                            metavar=("RED", "GREEN", "BLUE"), type=int, nargs=3)
        action.add_argument("-bl", "--blink", help="blink with a color",
                            metavar=("SPEED", "REPEAT", "RED", "GREEN", "BLUE"), type=int, nargs=5)
        action.add_argument("-fa", "--fade", help="fade with a color",
                            metavar=("SPEED", "REPEAT", "RED", "GREEN", "BLUE"), type=int, nargs=5)
        action.add_argument("-ra", "--random", help="random",
                            metavar=("SPEED", "REPEAT"), type=int, nargs=2)
        action.add_argument("-po", "--police", help="police",
                            metavar=("SPEED", "REPEAT"), type=int, nargs=2)
        args = parser.parse_args()
        self.neopix = NeoPixel(GPIO, LED_NUM,
                               brightness=args.brightness / 100, auto_write=False)
        if isfile("/tmp/mat_pix.json"):
            file_info = open("/tmp/mat_pix.json", "r")
            pixels = load(file_info)
            file_info.close()
            if len(pixels) == LED_NUM:
                i = 0
                for pixel in pixels:
                    self.neopix[i] = pixel
                    i = i + 1
        if args.clear:
            self.neopix.fill((0, 0, 0))
        elif not args.get is None:
            print(self.neopix[args.get])
        elif not args.set is None:
            self.neopix[args.set[0]] = (args.set[1], args.set[2], args.set[3])
        elif not args.setall is None:
            self.neopix.fill((args.setall[0], args.setall[1], args.setall[2]))
        elif not args.blink is None:
            self.blink(self, args.blink[0], args.blink[1],
                       args.blink[2], args.blink[3], args.blink[4])
        elif not args.fade is None:
            self.fade(self, args.fade[0], args.fade[1], args.fade[2], args.fade[3], args.fade[4])
        elif not args.random is None:
            self.random(self, args.random[0], args.random[1])
        elif not args.police is None:
            self.police(self, args.police[0], args.police[1])
        self.neopix.show()
        file_info = open("/tmp/mat_pix.json", "w")
        dump(list(self.neopix), file_info)
        file_info.close()

    def blink(self, speed, repeat, red, green, blue):
        tsleep = (100 - speed) / 40
        i = repeat
        while i > 0 or repeat == 0:
            self.neopix.fill((red, green, blue))
            self.neopix.show()
            sleep(tsleep)
            self.neopix.fill((0, 0, 0))
            self.neopix.show()
            sleep(tsleep)
            i = i - 1

    def fade(self, speed, repeat, red, green, blue):
        tsleep = (100 - speed) / 295
        i = repeat
        redi = red / 255
        greeni = green / 255
        bluei = blue / 255
        redv = 0
        greenv = 0
        bluev = 0
        while i > 0 or repeat == 0:
            self.neopix.fill((0, 0, 0))
            self.neopix.show()
            color = 255
            while color > 0:
                redv = redv + redi
                greenv = greenv + greeni
                bluev = bluev + bluei
                self.neopix.fill((round(redv), round(greenv), round(bluev)))
                self.neopix.show()
                sleep(tsleep)
                color = color - 1
            self.neopix.fill((red, green, blue))
            self.neopix.show()
            color = 255
            while color > 0:
                redv = redv - redi
                greenv = greenv - greeni
                bluev = bluev - bluei
                self.neopix.fill((round(redv), round(greenv), round(bluev)))
                self.neopix.show()
                sleep(tsleep)
                color = color - 1
            i = i - 1

    def random(self, speed, repeat):
        tsleep = (100 - speed) / 40
        i = repeat
        self.neopix[0] = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.neopix[1] = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.neopix[2] = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.neopix[3] = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.neopix[4] = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.neopix[5] = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.neopix[6] = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.neopix[7] = (randint(0, 255), randint(0, 255), randint(0, 255))
        while i > 0 or repeat == 0:
            self.neopix[randint(0, LED_NUM - 1)] = (randint(0, 255),
                                                    randint(0, 255),
                                                    randint(0, 255))
            self.neopix.show()
            sleep(tsleep)
            i = i - 1

    def police(self, speed, repeat):
        tsleep = (100 - speed) / 40
        i = repeat
        while i > 0 or repeat == 0:
            ibis = 3
            while ibis > 0:
                self.neopix.fill((0, 0, 0))
                self.neopix[0] = (0, 0, 255)
                self.neopix[1] = (0, 0, 255)
                self.neopix[2] = (0, 0, 10)
                self.neopix[3] = (255, 255, 255)
                self.neopix[4] = (255, 255, 255)
                self.neopix[5] = (10, 0, 0)
                self.neopix[6] = (255, 0, 0)
                self.neopix[7] = (255, 0, 0)
                self.neopix.show()
                sleep(tsleep / 5)
                self.neopix.fill((0, 0, 0))
                self.neopix[0] = (0, 0, 10)
                self.neopix[1] = (0, 0, 10)
                self.neopix[2] = (0, 0, 10)
                self.neopix[3] = (10, 10, 10)
                self.neopix[4] = (10, 10, 10)
                self.neopix[5] = (10, 0, 0)
                self.neopix[6] = (10, 0, 0)
                self.neopix[7] = (10, 0, 0)
                self.neopix.show()
                sleep(tsleep / 5)
                ibis = ibis - 1
            self.neopix.fill((0, 0, 0))
            self.neopix[0] = (0, 0, 255)
            self.neopix[1] = (0, 0, 255)
            self.neopix[2] = (0, 0, 10)
            self.neopix[3] = (255, 255, 255)
            self.neopix[4] = (255, 255, 255)
            self.neopix[5] = (10, 0, 0)
            self.neopix[6] = (255, 0, 0)
            self.neopix[7] = (255, 0, 0)
            self.neopix.show()
            sleep(tsleep)
            ibis = 3
            while ibis > 0:
                self.neopix.fill((0, 0, 0))
                self.neopix[0] = (0, 0, 10)
                self.neopix[1] = (0, 0, 255)
                self.neopix[2] = (0, 0, 255)
                self.neopix[3] = (10, 10, 10)
                self.neopix[4] = (10, 10, 10)
                self.neopix[5] = (255, 0, 0)
                self.neopix[6] = (255, 0, 0)
                self.neopix[7] = (10, 0, 0)
                self.neopix.show()
                sleep(tsleep / 5)
                self.neopix.fill((0, 0, 0))
                self.neopix[0] = (0, 0, 10)
                self.neopix[1] = (0, 0, 10)
                self.neopix[2] = (0, 0, 10)
                self.neopix[3] = (10, 10, 10)
                self.neopix[4] = (10, 10, 10)
                self.neopix[5] = (10, 0, 0)
                self.neopix[6] = (10, 0, 0)
                self.neopix[7] = (10, 0, 0)
                self.neopix.show()
                sleep(tsleep / 5)
                ibis = ibis - 1
            self.neopix.fill((0, 0, 0))
            self.neopix[0] = (0, 0, 10)
            self.neopix[1] = (0, 0, 255)
            self.neopix[2] = (0, 0, 255)
            self.neopix[3] = (10, 10, 10)
            self.neopix[4] = (10, 10, 10)
            self.neopix[5] = (255, 0, 0)
            self.neopix[6] = (255, 0, 0)
            self.neopix[7] = (10, 0, 0)
            self.neopix.show()
            sleep(tsleep)
            i = i - 1

if __name__ == "__main__":
    MatPix()
