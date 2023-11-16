with open("./Astro/S09/dataQB.txt","r") as f:
    lines = f.readlines()

for line in lines:
    if line != "\n":
        splitted = line.split()
        if splitted[0] == "radius":
            print(f"The moon radius is {splitted[1]}")