with open("./S12/QB.txt","r") as f:
    lines = f.readlines()
for line in lines:
    if line[0]!="#":
        splitted = line.split()
        if splitted[0] == "magnitude":
            print(splitted[1])