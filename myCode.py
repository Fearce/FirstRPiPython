from sense_hat import SenseHat
import time

sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
green = (0,255,0)


temp = sense.get_temperature()
printtemp = ("%.2f" % round(temp,2)) # Temperaturen rundet til 2 decimaler
# sense.show_message(str(printtemp))

x = 0
y = 0

while (x<8):
	

