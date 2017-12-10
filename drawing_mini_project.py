import turtle

def draw_triangle(runner):
    runner.forward(100)
    runner.right(45)
    runner.forward(100)
    runner.right(135)
    runner.forward(100)
    runner.right(45)
    runner.forward(100)
    runner.right(135)
        

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("silver")

    drawer = turtle.Turtle()
    drawer.color("brown")
    drawer.shape("arrow")

    for i in range(0, 36):      
        draw_triangle(drawer)
        drawer.right(10)
        
    drawer.right(90)
    drawer.forward(400)

    window.exitonclick()

draw_flower()
