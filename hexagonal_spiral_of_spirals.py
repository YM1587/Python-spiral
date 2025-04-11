import turtle
import math
from PIL import Image

# === Setup Screen ===
screen = turtle.Screen()
screen.title('Hexagon Spiral of Hexagon Spirals')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0, 0)  # Disable auto screen refresh for faster drawing

colors = ['red', 'orange', 'green', 'teal', 'blue', 'magenta']
alpha = 20  # Spiral twist angle

def draw_spiral(x, y, r, direction, first=False):
    if r < 1:
        return

    r_ratio = math.cos(math.radians(30)) / math.cos(math.radians(30 - alpha))
    d_ratio = math.sin(math.radians(30)) - r_ratio * math.sin(math.radians(30 - alpha))

    for i in range(6):
        if first:
            turtle.color(colors[i % len(colors)])
        
        px = x + r * math.cos(math.radians(direction))
        py = y + r * math.sin(math.radians(direction))

        r2 = r
        d = direction
        c = 0
        flag = False

        while True:
            dist = r2 * d_ratio
            if c > 10 and dist < 1:
                break

            if dist > 4:
                draw_spiral(px, py, dist * 0.4, d)
                turtle.up()
                turtle.goto(px, py)
                turtle.setheading(d + 180 - 60)
                turtle.forward(dist)
                px, py = turtle.xcor(), turtle.ycor()
            elif not flag:
                turtle.up()
                turtle.goto(px, py)
                turtle.down()
                flag = True
                turtle.setheading(d + 180 - 60)
                turtle.forward(dist)
            else:
                turtle.setheading(d + 180 - 60)
                turtle.forward(dist)

            r2 *= r_ratio
            d += alpha
            c += 1

        direction += 60

# === Draw the spiral ===
draw_spiral(0, 0, 800, 90, True)
screen.update()

# === Save to EPS then convert to PNG ===
canvas = turtle.getcanvas()
canvas.postscript(file="spiral.eps")  # Temporary EPS file

# Convert EPS to PNG using Pillow
img = Image.open("spiral.eps")
img.save("spiral.png", "PNG")

print("Spiral image saved as spiral.png")
turtle.done()
