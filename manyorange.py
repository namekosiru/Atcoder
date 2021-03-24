A, B, W = map(int, input().split())
max_num = 0
min_num = 0

W = W * 1000
w_min = W // B
min_num = min_num + w_min
min_s =W - min_num * B
if A <= min_s <= B or min_s <= 0:
    if min_s <= 0:
        pass
    else:
        min_num += 1
else:
    min_num = "UNSATISFIABLE"
w_max = W // A
max_num = max_num + w_max
max_s = W - max_num * A
if A <= max_s <= B or max_s <= 0:
    if W - max_num * A <= 0:
        pass
    else:
        min_num += 1
else:
    max_num = "UNSATISFIABLE"

if  type(max_num) is str or type(min_num) is str:
    print(max_num)
else:
    print(min_num, max_num)