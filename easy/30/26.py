H: int = int(input())

ans: int = 0
cnt: int = 1

while H > 0:
   ans += cnt
   H //= 2
   cnt *= 2
print(ans)
