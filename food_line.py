# Food line problem

lines = [3, 2, 5]

new_people = 4

for i in range(new_people):
    less_index = 0
    temp = lines[0]
   
    for j in range(len(lines)):
        if lines[j] < temp:
            temp = lines[j]
            less_index = j
    print(lines[less_index])
    lines[less_index] += 1

    
    #print(f"Person # {i}", lines)

