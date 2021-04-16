a, b, w = map(int,input().split())

weight = w * 1000 # 単位合わせ

flag = True # 組み合わせが起こり得るか判別フラグ

# 最大値を求める
tmp = weight // a # 余り切り下げ
if tmp * a <= weight and tmp * b >= weight:
    max_num = weight // a
else:
    flag = False

# 最小値を求める
tmp = -(-weight // b) # 余り切り上げ
if tmp * a <= weight and tmp * b >= weight:
    min_num = -(-weight // b)
else:
    flag = False

if flag:
    print(min_num, max_num)
else:
    print("UNSATISFIABLE")