s = input()

left, right = 0, len(s)-1

while right >= left:
    if s[left] == 'a' and s[right] == 'a':
        left += 1
        right -= 1
    elif s[right] == 'a':
        right -= 1
    else:
        if s[left] != s[right]:
            print("No")
            exit()
        else:
            left += 1
            right -= 1
    
    
print("Yes")