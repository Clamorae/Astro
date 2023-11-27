with open("./S11/EE.txt") as f:
    lines = f.readlines()
lines = lines[1:]

sorted = []
nan = []
for line in lines :
    splitted = line.split()
    if splitted[-1] == "NaN":
        nan.append(splitted)
    else:
        splitted[-1] = float(splitted[-1])
        if sorted == []:
            sorted.append(splitted)
        else:
            for i in range(len(sorted)):
                if sorted[i][-1] > splitted[-1]:
                    sorted.insert(i,splitted)
                    break
                if i == len(sorted)-1:
                    sorted.append(splitted)
sorted = nan+sorted
print(sorted)
