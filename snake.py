from turtle import Turtle

class Snake():
    def __init__(self):
        self.segments = []
        self.turtle_x_coordinate = 0
        self.create_snake()

    def create_turtle(self):
        new_segment = Turtle(shape= "square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x=self.turtle_x_coordinate, y=0)
        self.turtle_x_coordinate -= 20
        return new_segment

    def create_snake(self):
        for s in range(3):
            self.segments.append(self.create_turtle())

    def extend(self):
        last_segment = self.segments[-1]
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_segment)


    def move(self):
        for seg_num in range(len(self.segments)- 1, 0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()