MAX_LINES = 3

def shortest_line_index(lines, n):
    shortest = 0
    for j in range(n):
        if lines[j] < lines[shortest]:
            shortest = j
    return shortest

def solve(lines, n, m):
    for i in range(m):
        shortest = shortest_line_index(lines, n)
        print(lines[shortest], type(lines[shortest]))
        lines[shortest] += 1

lines = [0] * MAX_LINES
print(lines)
n = int(input("Enter number of lines:"))
m = int(input("Enter number of people:"))
for i in range(n):
    lines[i] = int(input(f"Number of people in line {i+1}: "))

print(lines)
solve(lines, n, m)

