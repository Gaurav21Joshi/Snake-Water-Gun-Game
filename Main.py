import random

# 1 for Snake
# -1 for Water
# 0 for Gun

computer = random.choice([-1, 0, 1])

you = int(input("Enter your choice (1 for Snake, -1 for Water, 0 for Gun): "))

# Dictionary to convert numbers into names
reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# Check for valid input
if you not in reverseDict:
    print("Invalid choice! Please enter 1, -1, or 0.")

else:
    print(f"You chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")

    # Game logic
    if computer == you:
        print("It's a Draw!")

    elif (
        (you == 1 and computer == -1)
        or (you == -1 and computer == 0)
        or (you == 0 and computer == 1)
    ):
        print("You Win!")

    else:
        print("You Lose!")