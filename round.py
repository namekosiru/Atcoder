x = input()

if "." in x:
    index_num = x.index(".")
    print(x[:index_num])
else:
    print(x)