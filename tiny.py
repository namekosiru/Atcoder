a_list = sorted(list(map(int, input().split())))
a1, a2, a3 = a_list[0], a_list[1], a_list[2]
if a3 - a2 == a2 - a1:
    print("Yes")
else:
    print("No")