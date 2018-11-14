from sense_hat import SenseHat
import time
import random

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
	points = 1
	lastDir = "up"
	x = 4
	y = 4
	foodX = random.randint(0,7)
	foodY = random.randint(0,7)
	color = white
	sense.set_pixel(x,y,color)
	while True:
		for event in sense.stick.get_events():
			if (event.action == "released"):
				if (event.direction == "up" and y>0):
					lastDir = "up"
					y -=1
					sense.clear()
				elif (event.direction == "down" and y<7):
					y +=1
					lastDir = "down"
					sense.clear()
				elif (event.direction == "left" and x>0):
					x -=1
					lastDir = "left"
					sense.clear()
				elif (event.direction == "right" and x<7):
					x +=1
					lastDir = "right"
					sense.clear()
				elif (event.direction == "middle"):
					x = 4
					points = 0
					y = 4
					sense.clear()
					
		if (x < 2 or x > 5):
			color = red
		elif (y < 2 or y > 5):
			color = blue
		else:
			color = white
		if (foodX == x and foodY == y):
			points += 1
			foodX = random.randint(0,7)
			foodY = random.randint(0,7)
			sense.clear()
		sense.set_pixel(foodX,foodY,yellow)
		for pts in range(points):
			if (lastDir == "up"):
				sense.set_pixel(x,y+pts,color)
			if (lastDir == "down"):
				sense.set_pixel(x,y-pts,color)
			if (lastDir == "left"):
				sense.set_pixel(x+pts,y,color)
			if (lastDir == "right"):
				sense.set_pixel(x-pts,y,color)
		
MakeDotJoystick()
	

