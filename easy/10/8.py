a, b = input().split()


for i in range(1, 10**5):
    if i**2 == int(a+b):
        print("Yes")
        exit()
print("No")