from sense_hat import SenseHat
import time

sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
green = (0,255,0)


temp = sense.get_temperature()
printtemp = ("%.2f" % round(temp,2)) # Temperaturen rundet til 2 decimaler


global x
x = 0
global y 
y = 0
global color 
color = red

def ChangeColor():
	global color
	if color == red:
		color = blue
	elif color == blue:
		color = yellow
	elif color == yellow:
		color = green
	elif color == green:
		color = red

#while (y<8):
#	DoColors(x,y,color)
#	y = y+1
	
while (y<=3):
	while(x<8):
		sense.set_pixel(x,y,color)
		time.sleep(0.2)
		x += 1
		if (x==8):
			ChangeColor()
	time.sleep(0.2)
	y += 1
	x = 0

while True:
	for event in sense.stick.get_events():
    # print(event.direction, event.action)
		if (len(event.direction) > 2):
			sense.show_message(str(printtemp))
		
#sense.show_message(str(printtemp))
	

