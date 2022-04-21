"""
Tower of Hanoi
Code inpired by video: Recursion 'Super Power' (in Python) - Computerphile
https://www.youtube.com/watch?v=8lhxIOAfDss
"""


STEPS = 1
positions = ["A", "B", "C"]


def move(move_from: str, move_to: str):
    """
    Instruction to move one disc from one position to another.

    :param move_from: Starting position.
    :param move_to: End position.
    """
    global STEPS
    print(f"Step {STEPS:3}:\tMove disc from {move_from} to {move_to}!")
    STEPS += 1


def hanoi(discs: int, move_from: str, move_via: str, move_to: str):
    """
    Solves the Tower of Hanoi problem.

    :param discs: Number of discs to move.
    :param move_from: Starting position.
    :param move_via: Spare position.
    :param move_to: End position.
    """
    # Check for negative discs.
    if discs < 0:
        print("Number of discs should not be negative.")
    # Have a limit of 9 discs.
    elif discs > 9:
        print("Over 1,000 moves! Try 1-9 discs.")
    # Do nothing when zero discs.
    elif discs == 0:
        pass
    else:
        # Move all but one number_of_discs to spare position.
        hanoi(discs - 1, move_from, move_to, move_via)
        # Move last number_of_discs to final position.
        move(move_from, move_to)
        # Move remaining discs to final position.
        hanoi(discs - 1, move_via, move_from, move_to)


if __name__ == '__main__':
    print("Welcome to the Tower of Hanoi solver.")
    number_of_discs = int(input("How many discs? "))
    hanoi(number_of_discs, *positions)
