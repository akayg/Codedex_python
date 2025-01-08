guess = 0
tries = int(input("No of tries: "))

while tries != 0 and guess != 6:  # Use 'and' instead of 'or' for correct logic
    print(f"{tries} tries left")
    guess = int(input("Enter your guess: "))
    tries -= 1  # Reduce tries by 1 after each guess

if guess == 6:
    print("You got it!")
else:
    print("Out of tries! The correct number was 6.")
