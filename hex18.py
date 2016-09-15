import turtle
turtle.shape('turtle')
for i in range(3,11):
	turtle.pendown()
	for j in range(0,i):
		turtle.left(180*(i-2)/i+180)
		turtle.forward(40+20*(i-2))
	turtle.penup()
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(10)
	turtle.right(90)
