class Rocket:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def current_position(self):
        print(f"Current Position: ({self.x}, {self.y})")

# Testing the Rocket class
rocket = Rocket()

rocket.move_up()
rocket.move_right()
rocket.move_down()
rocket.move_left()
rocket.move_left()

rocket.current_position()