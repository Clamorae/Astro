with open("./Astro/S08/data2.txt","r") as f:
    lines = f.readlines()

for line in lines:
    splitted = line.split()
    if splitted[0] == "luminosity":
        print(f"The luminosity of the sun is {splitted[1]}")