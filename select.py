s = input()
count_o = 0
count_ = 0
for i in s:
    if i == "o":
        count_o+= 1
    if i == "?":
        count_ += 0
    if count_o >= 5:
        print(0)
        exit()

total = 0
total += count_o ** 4

