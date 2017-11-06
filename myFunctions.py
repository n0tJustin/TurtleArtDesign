def box (t,r,g,b):
    t.begin_fill()
    t.color(r,g,b)
    for times in range(4):
        t.forward(10)
        t.right(90)
    t.end_fill()

def jump (t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
