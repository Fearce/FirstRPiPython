from sense_hat import SenseHat
import time

sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
green = (0,255,0)


temp = sense.get_temperature()
printtemp = ("%.2f" % round(temp,0)) # Temperaturen rundet til 2 decimaler


x = 0
y = 0
color = red

def DoColors(a,b,c):
	while (a<8):
		sense.set_pixel(a,b,c)
		time.sleep(0.2)
		a = a+1
		if c == red:
			c = blue
		elif c == blue:
			c = yellow
		elif c == yellow:
			c = green
		elif c == green:
			c = red

#while (y<8):
#	DoColors(x,y,color)
#	y = y+1
	

sense.show_message(str(printtemp))
	

