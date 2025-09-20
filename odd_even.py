n = 4
odd = 1
even = 2

for row in range(n):
    for col in range(n):
        if row % 2 == 0:
            print(odd, end=' ')
            odd += 2
        else:
            print(even, end=' ')
            even += 2
    print()
