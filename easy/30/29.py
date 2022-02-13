s = input()

NUMBER_753 = 753
ans: int = 10000

for i in range(len(s)-2):
    number: int = int(s[i:i+3])
    if (diff := abs(number - NUMBER_753)) < ans:
        ans = diff
print(ans)