from gpiozero import LED,Button
from signal import pause

btn = Button(17, pull_up=True)
led = LED(21)
btn.wait_for_press()
btn.when_pressed = led.on
btn.when_released = led.off

pause()

def function1(led):
	print("pressed")
def function2(led):
	print("released")

while True:
	btn.when_pressed = function1
	btn.when_released = function2
