s = input()

moji_list: list = []

for si in s:
    if si in moji_list:
        print("no")
        exit()
    moji_list.append(si)

print("Yes")