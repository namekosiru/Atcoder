N = int(input())
name_dict = {}
for _ in range(N):
    name, height = input().split()
    name_dict[name] = int(height)

name_sorted = sorted(name_dict.items(), key=lambda x:x[1])

print(name_sorted[-2][0])