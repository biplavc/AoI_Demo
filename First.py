# /media/biplav/Biplav_2/CollegeStuff/Research/DrReed/AgeofInformation/demo/game/Space_Invaders/program/SpaceInvaders

import os
import random
import turtle
turtle.fd(0)
turtle.speed(1)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)
class Game():	
	def draw_border(self):
		#Draw border
		self.pen = turtle.Turtle()
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300, 300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()

game = Game()
game.draw_border()

bulletstate1 = "ready"
bulletstate2 = "ready"

def enemy1_fire():
	#the bullet will travel up from the player's position
	global bulletstate1 # enable modifying global var from inside of function
	if bulletstate1 == "ready":
		bulletstate1 = "fire"
		x = enemy1.xcor()
		y = enemy1.ycor()
		bullet1.speed = 0
		bullet1.setposition(x,y) # bullet will appear just above the player
        bullet1.showturtle()
        bullet1.speed = 6
		# the movement of the bullet will be defined in the game loop

def enemy2_fire():
	#the bullet will travel up from the player's position
	global bulletstate2 # enable modifying global var from inside of function
	if bulletstate2 == "ready":
		bulletstate2 = "fire"
		x = enemy2.xcor()
		y = enemy2.ycor()
		bullet2.speed = 0
		bullet2.setposition(x,y) # bullet will appear just above the player
        bullet2.showturtle()
        bullet2.speed = 6
		# the movement of the bullet will be defined in the game loop
class Player(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 6
		self.left(90)
	
	def move(self):
		self.fd(10)
	
	def turn_left(self):
		self.lt(30)
	def turn_right(self):
		self.rt(30)
	def accelerate(self):
		self.move()
		self.speed = self.speed + 1
class Enemy1(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(3)
		self.goto(startx, starty)
		self.speed = 6
	
	shoot = 8 # shoots after 4 interval

  	def move(self):
		self.lt(90)
		self.fd(150)
		self.shoot = self.shoot - 1
		if self.shoot==0:
			enemy1_fire() #shoot towards player
			self.shoot = 8
class Enemy2(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 3

	shoot = 4 # shoots after 2 interval

	def move(self):
		self.fd(100)
		self.rt(30)
		self.shoot= self.shoot-1
		if self.shoot==0:
			enemy2_fire() #shoot towards player
			self.shoot = 4

enemy1 = Enemy1("circle", "red", 50, -50)
enemy2 = Enemy2("square", "blue", -10, 200)
player = Player("triangle", "white", 0, -290)


#key bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
#turtle.onkey(player.brake,"Down")

# create a bullet for the enemy1
bullet1  = turtle.Turtle()
bullet1.color("yellow")
bullet1.shape("triangle")
bullet1.penup()
bullet1.shapesize(0.3,0.3)
bullet1.hideturtle() 
bullet1.speed = 1

# create a bullet for the enemy2
bullet2  = turtle.Turtle()
bullet2.color("yellow")
bullet2.shape("square")
bullet2.penup()
bullet2.shapesize(0.4,0.4) 
bullet2.hideturtle() 
bullet2.speed = 1



while True:
	print (enemy1.shoot, enemy2.shoot)
	enemy1.move()
	enemy2.move()


	if bulletstate1=="fire":
		y = bullet1.ycor()
		y = y - 900
		bullet1.sety(y)

	if bulletstate2=="fire":
		y = bullet2.ycor()
		y = y - 900
		bullet2.sety(y)

	if (bullet1.ycor()>275 or bullet1.xcor()>275 or bullet1.ycor()<-275 or bullet1.xcor()<-275):
		bullet1.hideturtle()
		bulletstate1="ready"

	
	if (bullet2.ycor()>275 or bullet2.xcor()>275 or bullet2.ycor()<-275 or bullet2.xcor()<-275):
		bullet2.hideturtle()
		bulletstate2="ready"

delay = raw_input("Press enter to finish. > ")