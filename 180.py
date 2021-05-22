s_char = list(input())[::-1]
for s in s_char:
    if s == "6":
        print(9, end="") 
    elif s == "9":
        print(6, end="")
    else:
        print(s, end="")