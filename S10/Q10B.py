with open("./Astro/S10/E02.txt","r") as f:
    lines = f.readlines()

for line in lines:
    if line !="#":
        splitted = line.split()
        if splitted[0] == "escape_velocity":
            print(f"The escape velocity of mars is {splitted[1]}")