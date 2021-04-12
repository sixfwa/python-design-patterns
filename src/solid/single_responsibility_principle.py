"""
The Single Responsibility Principle

A class should have one, and only one, reason to change.
"""

food_bowl = 10


class Cat:
    def __init__(self, name: str):
        self.name = name
        self.food_level = 30
        self.cleanliness_level = 50

    def meow(self):
        print("meow")

    def eat(self):
        self.food_level += 10

    def sleep(self):
        print(f"{self.name} is now sleeping")

    # breaking SRP
    # def prepare_food_bowl(self):
    #     food_bowl += 10

    # # breaking SRP
    # def shower(self):
    #     self.cleanliness_level += 30


class Owner:
    """
    The person that takes care of a cat
    """

    @staticmethod
    def prepare_food_bowl():
        food_bowl += 10

    @staticmethod
    def clean_cat(cat: Cat):
        cat.cleanliness_level += 30


cat = Cat("fred")
owner = Owner()

print(f"cat clean level: {cat.cleanliness_level}")
owner.clean_cat(cat)
print(f"cat clean level: {cat.cleanliness_level}")
