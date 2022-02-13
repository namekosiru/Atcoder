s = set(input())

ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

for alphabet in ALPHABET:
    if alphabet not in s:
        print(alphabet)
        exit()
print("None")

