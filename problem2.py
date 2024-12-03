with open("inputs/problem2.txt", "r") as f:
    reports = [list(map(int, line.split())) for line in f]

def is_safe(l):
    increasing = decreasing = True
    for i in range(len(l) - 1):
        diff = l[i+1] - l[i]
        if not (1 <= abs(diff) <= 3):
            return False
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
    return increasing or decreasing

safe_count = sum(is_safe(report) for report in reports)
print(safe_count)

def is_safe_with_removal(report):
    if is_safe(report):
        return True
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

safe_count2 = sum(is_safe_with_removal(report) for report in reports)
print(safe_count2)