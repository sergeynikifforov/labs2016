import turtle
turtle.shape('turtle')
turtle.speed(10)
for i in range(10):
	for j in range(180):
		turtle.left(1)
		turtle.forward(1)
	for j in range(180):
		turtle.left(1)
		turtle.forward(1/10)

