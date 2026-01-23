import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")
class Dice:
    """Represents a group of dice that can be rolled."""

    def __init__(self, num_dice):
        """
        Initializes the dice list based on the number of dice.
        :param num_dice: Number of dice to create
        """
        self.values = [0] * num_dice

    def roll(self):
        """
        Rolls each die and assigns a random value from 1 to 6.
        """
        for i in range(len(self.values)):
            self.values[i] = random.randint(1, 6)

    def get_total(self):
        """
        Returns the sum of all dice values.
        :return: Total of the dice
        """
        return sum(self.values)

    def print_dice(self):
        """
        Prints the dice horizontally using ASCII art.
        """
        for line in range(5):
            for value in self.values:
                print(dice_art[value][line], end="")
            print()

num_of_dice = int(input("How many dice?: "))

dice = Dice(num_of_dice)
dice.roll()

dice.print_dice()
print(f"Total: {dice.get_total()}")