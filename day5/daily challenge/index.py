import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area:.2f})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius



c1 = Circle(radius=30)
c2 = Circle(diameter=80)
c3 = Circle(radius=50)
c4 = c1 + c3  

circles = [c1, c2, c3, c4]
circles.sort()

print("Cercles triés :")
for c in circles:
    print(c)


t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "green", "blue", "yellow", "purple", "cyan"]

for i, circle in enumerate(circles):
    t.penup()
    t.goto(0, -circle.radius) 
    t.pendown()
    t.pencolor(colors[i % len(colors)])
    t.circle(circle.radius)

turtle.done()
