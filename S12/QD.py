with open("./S12/QD.txt") as f:
    lines = f.readlines()
lines = lines[1:]

sorted = []
for line in lines :
    splitted = line.split()
    splitted[1] = float(splitted[1][-4:-1]) + 100 * float(splitted[1][-7:-5])
    if sorted == []:
        sorted.append(splitted)
    else:
        for i in range(len(sorted)):
            if sorted[i][1] > splitted[1]:
                sorted.insert(i,splitted)
                break
            if i == len(sorted)-1:
                sorted.append(splitted)

print(sorted)

