def name(n):
    b = set()
    for i in n:
        for j in range(i[0], i[1]):
            b.add(j)
    print(b)
    return(len(b))

pairs = []
num_of_pairs = int(input())
for i in range(num_of_pairs):
    pairs.append([int(input()), int(input())])
print(pairs)
print(name(pairs))
