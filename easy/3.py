n, a, b = map(int, input().split())
s = input()

win_count = 0
b_count = 0
for i in range(n):
    if s[i] == "c":
        print("No")
    elif s[i] == "a":
        if a+b > win_count:
            print("Yes")
            win_count += 1
        else:
            print("No")
    else:
        if a+b > win_count:
            if b_count < b:
                print("Yes")
                b_count += 1
                win_count += 1
            else:
                print("No")
        else:
            print("No")
