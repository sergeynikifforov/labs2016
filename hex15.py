import turtle
turtle.shape('turtle')
n=int(input())
for i in range(1,n+1):
	turtle.pendown()
	turtle.left(360/n)
	turtle.forward(40)
	turtle.left(180)
	turtle.penup()
	turtle.forward(40)
	turtle.left(180)
	
