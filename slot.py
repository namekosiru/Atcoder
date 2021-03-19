chars = input()

for i in chars:
    if chars[0] != i:
        print("Lost")
        exit()
print("Won")