n = input()
int_n = int(n)
len_number = len(n) 

if 1<=int_n<=9:
    print(0)
    exit()
center = len_number // 2
total = 0

right = 10 ** (center - 1)
left  = 10 ** (center - 1)

while True:
    char = int(str(left) + str(right))
    if char > int_n:
        break
    left += 1
    right += 1
    total += 1
for i in range((len_number - 2)//2):
    total += 9 *(10 ** i)
print(total)