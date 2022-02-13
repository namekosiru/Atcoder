a, b = map(int, input().split())

ans: int = 0

def judge_kibun(number_str: str) -> bool:
    length: int = len(number_str)
    for i in range(length//2):
        if  number_str[i] != number_str[length-i-1]:
            return False
    return True 

for number in range(a, b+1):
    number_str: str = str(number)
    if judge_kibun(number_str): ans += 1
print(ans)
