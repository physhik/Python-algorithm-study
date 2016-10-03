import turtle
import random
def tree(branchLen,t):
    if branchLen > 5:
		if branchLen>=100:
			t.pensize(4)
		elif branchLen <100 and branchLen >= 70:
			t.pensize(3)
		elif branchLen <70 and branchLen >= 40:
			t.pensize(2)
		elif branchLen <40 and branchLen >= 20:
			t.pensize(1)
		else:
			t.pensize(0.5)
		
		angle1=random.randint(15,45)
	
		t.forward(branchLen)
		t.right(angle1)
		
		angle2=random.randint(30,90)	
		tree(branchLen-10,t)
		t.left(angle2)
		
		tree(branchLen-15,t)
		t.right(angle2-angle1)
		t.backward(branchLen) 
		
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(100,t)
    myWin.exitonclick()

main()