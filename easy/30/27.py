n, a, b = map(int, input().split())

ans: int = 0
ans = (n // (a+b)) * a

if (rest:=n % (a+b)) > a:
    ans += a
else:
    ans += rest
print(ans)