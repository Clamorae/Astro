with open("./S11/EB.txt") as f:
    lines = f.readlines()

for line in lines:
    if line != "#":
        splitted = line.split()
        if splitted[0] == "density":
            print(f"Jupiter density is {splitted[1]} {splitted[3]}")