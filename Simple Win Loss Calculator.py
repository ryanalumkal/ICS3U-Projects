win = 0
loss = 0


for i in range(10):
    result = input("Enter result of game (W) or (L): ")
    if result == 'W':
        win += 1
    elif result == 'L':
        loss += 1

print("You won", str(win), "game(s)")
print("You lost", str(loss), "game(s)")