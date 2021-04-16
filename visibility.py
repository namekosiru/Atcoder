h, w, x, y = map(int,input().split())
x -= 1
y -= 1

S = []
for i in range(h):
    S.append(input())

# 座標(x,y)自身もカウントするので初期値は1
ans = 1

# 座標(x,y+1)から下方向の探索
for i in range(1,101):
    if y+i >= w or S[x][y+i] == "#":
        break
    if S[x][y+i] != "#":
        ans += 1

# 座標(x,y-1)から上方向の探索
for i in range(1,101):
    if y-i < 0 or S[x][y-i] == "#":
        break
    if S[x][y-i] != "#":
        ans += 1

# 座標(x+1,y)から右方向の探索
for j in range(1,101):
    if x+j >= h or S[x+j][y] == "#":
        break
    if S[x+j][y] != "#":
        ans += 1

# 座標(x-1,y)から左方向の探索
for j in range(1,101):
    if x-j < 0 or S[x-j][y] == "#":
        break
    if S[x-j][y] != "#":
        ans += 1

print(ans)