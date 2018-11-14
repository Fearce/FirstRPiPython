from sense_hat import SenseHat
import time

sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)


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

def PrettyLines():
	global y
	global x
	while (y<=3): #udfyld rækkerne y0 til y3
		while(x<8): #fyld x0-7
			sense.set_pixel(x,y,color)
			time.sleep(0.2)
			x += 1
			if (x==8): #skift farve når x er 8
				ChangeColor()
		time.sleep(0.2)
		y += 1
		x = 0
#PrettyLines()

def old(): #shows temp on joystick use
	while True:
		for event in sense.stick.get_events():
			print(event.direction, event.action)
			if (len(event.direction) > 2):
				sense.show_message(str(printtemp))
		
#old()

def DisplayTempByColor(): #shows temp in a color
	while True:
		color = red
		temp = int(sense.get_temperature())
		if temp<0:
			color = blue
		elif temp>0 and temp<20:
			color = green
		elif temp>=20:
			color = red
		sense.show_message(str(temp),text_colour=color)
		
#DisplayTempByColor()
#sense.show_message(str(printtemp))

def MakeDotJoystick():
	x = 4
	y = 4
	color = white
	sense.set_pixel(x,y,color)
	while True:
		for event in sense.stick.get_events():
			if (event.action == "released"):
				if (event.direction == "up"):
					y -=1
					sense.clear()
				elif (event.direction == "down"):
					y +=1
					sense.clear()
				elif (event.direction == "left"):
					x -=1
					sense.clear()
				elif (event.direction == "right"):
					x +=1
					sense.clear()
		if (x < 2 or x > 5):
			color = red
		if (y < 2 or y > 5):
			color = blue
		sense.set_pixel(x,y,color)
		
MakeDotJoystick()
	

