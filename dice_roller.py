import time,random,os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_dice():
    print("Rolling the dice",end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".",end="",flush=True)
    print()

    for _ in range(5):
        face= random.randint(1,6)
        print_dice_face(face)
        time.sleep(0.5)
        clear_console()
    final_roll=random.randint(1,6)
    print("the dice lands on:")
    print_dice_face(final_roll)

def print_dice_face(number):
    dice_faces = {
        1: ["+-------+",
            "|       |",
            "|   o   |",
            "|       |",
            "+-------+"],
        2: ["+-------+",
            "| o     |",
            "|       |",
            "|     o |",
            "+-------+"],
        3: ["+-------+",
            "| o     |",
            "|   o   |",
            "|     o |",
            "+-------+"],
        4: ["+-------+",
            "| o   o |",
            "|       |",
            "| o   o |",
            "+-------+"],
        5: ["+-------+",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            "+-------+"],
        6: ["+-------+",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            "+-------+"]
    }
    for line in dice_faces[number]:
        print(line)

if __name__ == "__main__":
    while True:
        user_input = input("Press Enter to roll the dice or type 'q' to quit: ").lower()
        if user_input == 'q':
            print("Goodbye!")
            break
        clear_console()
        roll_dice()
        print()
        if input("Roll again? (y/n): ").lower() != 'y':
            print("Goodbye!")
            break
