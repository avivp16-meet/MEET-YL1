import turtle
turtle.speed(0)
turtle.hideturtle()
a=2
b="z"
def circle (color,x,y,size):
    turtle.begin_fill()
    turtle.color(color)
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.circle(size)
    turtle.end_fill()
    turtle.penup()
    #green
def green_c1(x,y):
    circle("green",x,y,1)

def green_c20(x,y):
    circle("green",x,y,20)

def green_c40(x,y):
    circle("green",x,y,40)
    #blue
def blue_c1(x,y):
    circle("green",x,y,1)

def blue_c20(x,y):
    circle("green",x,y,20)

def blue_c40(x,y):
    circle("green",x,y,40)

def d(x,y):
    global a
    if(a ==2):
        green_c40(x,y)
    elif (a==3):
        green_c35(x,y)
def key ():
 turtle.getscreen().onkeypress(green_c1,"z")
 if(b=="z"):
    

      
turtle.onscreenclick(green_c1, btn=1, add=True)

turtle.getscreen().onkeypress(green_c1,"z")
turtle.getscreen().onkeypress(green_c5,"x")
turtle.getscreen().onkeypress(green_c10,"c")
turtle.getscreen().onkeypress(green_c15,"v")
turtle.getscreen().onkeypress(green_c20,"b")
turtle.getscreen().onkeypress(green_c25,"n")
turtle.getscreen().onkeypress(green_c30,"m")
turtle.getscreen().onkeypress(green_c35,"1")
turtle.getscreen().onkeypress(green_c40,"2")
turtle.getscreen().onkeypress(blue_c1,"a")
turtle.getscreen().onkeypress(blue_c5,"s")
turtle.getscreen().onkeypress(blue_c10,"d")
turtle.getscreen().onkeypress(blue_c15,"f")
turtle.getscreen().onkeypress(blue_c20,"g")
turtle.getscreen().onkeypress(blue_c25,"h")
turtle.getscreen().onkeypress(blue_c30,"j")
turtle.getscreen().onkeypress(blue_c35,"k")
turtle.getscreen().onkeypress(blue_c40,"l")






turtle.mainloop
