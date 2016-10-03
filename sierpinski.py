import turtle

t=turtle.Turtle()


def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()
	
def sierpinski(p, index, myTurtle):
	colormap = ['blue','red','green','white','yellow','violet','orange']
	color=colormap[index]
	drawTriangle(p, color, myTurtle)
	
	nextPoints1=[[0,0],[0,0],[0,0]]
	nextPoints1[0]=p[0]
	nextPoints1[1]=[p[0][0]/2+p[1][0]/2,p[0][1]/2+p[1][1]/2] # 0 +1
	nextPoints1[2]=[p[0][0]/2+p[2][0]/2,p[0][1]/2+p[2][1]/2] #0+ 2
	
	nextPoints2=[[0,0],[0,0],[0,0]]
	nextPoints2[0]=p[1]
	nextPoints2[2]=[p[0][0]/2+p[1][0]/2,p[0][1]/2+p[1][1]/2]
	nextPoints2[1]=[p[1][0]/2+p[2][0]/2,p[1][1]/2+p[2][1]/2]
	
	nextPoints3=[[0,0],[0,0],[0,0]]
	nextPoints3[0]=p[2]
	nextPoints3[2]=[p[0][0]/2+p[2][0]/2,p[0][1]/2+p[2][1]/2]
	nextPoints3[1]=[p[1][0]/2+p[2][0]/2,p[1][1]/2+p[2][1]/2]
	
	if index < 5:
		sierpinski(nextPoints1, index+1, myTurtle)
		sierpinski(nextPoints2, index+1, myTurtle)
		sierpinski(nextPoints3, index+1, myTurtle)

	
	
def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   p = [[-100,-50],[0,100],[100,-50]]

   sierpinski(p, 0 ,myTurtle)
   myWin.exitonclick()



main()




	