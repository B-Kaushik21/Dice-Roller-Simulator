import random
import time
import sys

def print_dice_animation():
    frames = [
        "[    ]",
        "[ *  ]",
        "[ ** ]",
        "[*** ]",
        "[****]"
    ]
    for frame in frames:
        sys.stdout.write(f"\rRolling... {frame}")
        sys.stdout.flush()
        time.sleep(1)

def roll_dice():
    print("\nGet ready to roll the dice!")
    print_dice_animation()
    result = random.randint(1, 6)
    sys.stdout.write(f"\rYou rolled a {result}!          \n")
    sys.stdout.flush()

while True:
    input("Press Enter to roll the dice (or Ctrl+C to quit)")
    roll_dice()