h, w = map(int, input().split())

if h==1 or w==1:
    print(1)
    exit()

ans = h*w//2

if (h*w)%2==1:
    ans += 1
print(ans)