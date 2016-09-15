import turtle
def f(n):
	for i in range(1,n+1):
		turtle.left(180-180/n)
		turtle.forward(60)
f(5)
turtle.penup()
turtle.goto(60,0)
turtle.pendown()
f(11)

