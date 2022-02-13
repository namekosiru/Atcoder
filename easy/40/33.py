a, b = map(int, input().split())
s = input()

NUMBERS = "0123456789"

for ai in s[:a]:
    if ai in NUMBERS:
        continue
    print("No")
    exit()
if s[a] != "-":
    print("No")
    exit()

for bi in s[a+1:]:
    if bi in NUMBERS:
        continue
    print("No")
    exit()

print("Yes")