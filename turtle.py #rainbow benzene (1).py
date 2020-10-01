# Python program to draw 
# Rainbow Benzene 
# Using Turtle Programming 
import turtle  #This line will import turtle library in Python
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') #Here we choose the background colour to be black
for x in range(360): 
	t.pencolor(colors[x%6]) 
	t.width(x/100 + 1) 
	t.forward(x) 
	t.left(59) 