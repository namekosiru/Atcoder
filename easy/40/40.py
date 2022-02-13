a, b = map(int, input().split())

if a >= 1 and b >= 1:
    print("Positive")
elif b >= 0 and a <= 0:
    print("Zero") 
elif a <= -1 and b <= -1:
    if (b - a + 1) % 2 == 0:
        print("Positive")
    else:
        print("Negative")