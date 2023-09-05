'''3. Create a Motorcycle class with the following attributes:
brand, model, year, and speed. The Motorcycle class should have
the following methods: accelerate, brake and display_speed.
The accelerate method should increase the speed by 5, and
the brake method should decrease the speed by 5. Remember
that the speed cannot be negative.'''


class Motorcycle:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed = max(0, self.speed + 5)

    def brake(self):
        self.speed = max(0, self.speed - 5)

    def display_speed(self):
        print(f"Current speed of the {self.year} {self.brand} {self.model}: {self.speed} km/h")


def main():
    honda_dragstar = Motorcycle('Honda', 'DragStar', 2022, 90)

    honda_dragstar.display_speed()

    honda_dragstar.accelerate()
    honda_dragstar.display_speed()

    honda_dragstar.brake()
    honda_dragstar.display_speed()


if __name__ == "__main__":
    main()
