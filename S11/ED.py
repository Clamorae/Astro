with open("./S11/ED.txt") as f:
    lines = f.readlines()
lines = lines[1:]

sorted = []
for line in lines :
    splitted = line.split()
    splitted[-2] = float(splitted[-2])
    if sorted == []:
        sorted.append(splitted)
    else:
        for i in range(len(sorted)):
            if sorted[i][-2] > splitted[-2]:
                sorted.insert(i,splitted)
                break
            if i == len(sorted)-1:
                sorted.append(splitted)

print(sorted)
