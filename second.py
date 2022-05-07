import random
S = []

while len(S) != 30:
    x = random.randint(1, 100)
    if x % 2 == 0:
        S.append(x)

print(S, len(S))
