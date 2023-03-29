from gpiozero import LED,Button
from signal import pause
from time import sleep

button = Button(21)
slide = Button(22)

green = LED(6)
red = LED(19)
blue = LED(23)

things = [green, red, blue]

def things_on():
       for thing in things:
               thing.value = 1
#               print(thing.value)

def things_off():
       for thing in things:
               thing.value = 0
while True:
        button.when_pressed = things_on
        button.when_released = things_off
	slide.when_pressed = things_on
	slid
