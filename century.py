N = int(input())

if N % 100 == 0:
    print(N // 100)
else:
    century = N // 100
    print(century+1)