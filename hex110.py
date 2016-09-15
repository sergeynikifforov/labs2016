import turtle
turtle.shape('turtle')
turtle.speed(10)
k=1
for i in range(10):
	for j in range(360):
		turtle.left(1)
		turtle.forward(k)
	for j in range(360):
		turtle.right(1)
		turtle.forward(k)
	k+=1 
