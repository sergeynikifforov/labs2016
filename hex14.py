import turtle
turtle.shape('turtle')
for i in range(1,10):
	turtle.pendown()
	for j in range(1,5):
		turtle.forward(i*20)
		turtle.left(90)
	turtle.penup()
	turtle.right(90)
	turtle.forward(10)
	turtle.right(90)
	turtle.forward(10)
	turtle.left(180)
	


