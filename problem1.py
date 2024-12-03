with open("inputs/problem1.txt", "r") as f:
    inputs = f.read().splitlines()

sum1, sum2 = zip(*[map(int, line.split()) for line in inputs])
sum1, sum2 = sorted(sum1), sorted(sum2)

distance = sum(abs(a - b) for a, b in zip(sum1, sum2))
sum2_count = {num: sum2.count(num) for num in set(sum2)}
similarity = sum(a * sum2_count[a] for a in sum1 if a in sum2_count)

print(distance)
print(similarity)