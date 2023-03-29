from gpiozero import LED,Button 
from signal import pause 
import time 

led = LED(21) 
button = Button(17)
 
button.when_pressed = led.on 
button.when_released = led.off 

while True:
	button.wait_for_press() 
	start = time.time() 

	button.wait_for_release() 
	end = time.time()

	print("pressed for: ", end-start)
