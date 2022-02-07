a, b, c = map(int, input().split())

if a==b==c and (a%2==0 and b%2==0 and c%2==0):
    print(-1)
    exit()
ans = 0
while a%2==0 and b%2==0 and c%2==0:
    a_copy, b_copy = a, b
    a = b_copy//2 + c//2
    b = a_copy//2 + c//2
    c = a_copy//2 + b_copy//2
    ans += 1
print(ans)
