from gpiozero import LED,Button
from signal import pause
from time import sleep

button = Button(21, pull_up=True)
slide = Button(22, pull_up=True)

green = LED(6)
red = LED(19)
blue = LED(23)

things = [green, red, blue]

def slide_on():
#slide on
	if slide.value == 1:			#if slide is on green is on else red is on
		green.on()
	else:
		red.on()

def btn_on ():
#button
	if button.value == 0:			#if button is off red and blue will be on
		red.on()
	else:
		blue.on()
def things_on():				#turns all leds on
	for thing in things:
		thing.on()
def things_off():				#turns all leds off
	for thing in things:
		thing.off()
#		print(thing.value)

while True:
	button.when_pressed = slide_on
	button.when_released = things_off
	slide.when_pressed = btn_on
	slide.when_released = things_off
	button.when_pressed = things_on

pause()
