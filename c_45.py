S = input()
n = len(S) -1

ans = 0

for i in range(2 ** n):
	f = S[0] # この場合は1
	for j in range(n):
		if i >> j & 1:
			f += '+' #　文字列に+を付与
		f += S[j + 1] # 次の数を追加
	ans += sum(map(int, f.split("+")))
print(ans)