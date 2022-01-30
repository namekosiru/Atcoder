s = input()

for i in range(len(s)//2):
    if s[i] == s[len(s)-1-i]:
        continue
    if s[i] != s[len(s)-1-i] and s[len(s)-1-i] == "a":
        s = "a" + s
    else:
        print("No")
        exit()
    
print("Yes")