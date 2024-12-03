import re

with open("inputs/problem3.txt", "r") as f:
    inputs = f.read().splitlines()

regex = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(regex, "\n".join(inputs))


sum = 0
status = 1
for match in matches:
    if match[:3] == "mul" and status:
        m, n = re.findall(r"\d+", match)
        sum += int(m) * int(n)
    elif match == "do()":
        status = 1
    elif match == "don't()":
        status = 0

print(sum)