with open("./Astro/S10/E04","r") as f:
    lines = f.readlines()

lines = lines[1:]
mag_list = []
for line in lines:
    splitted = line.split()
    mag_list.append(float(splitted[4]))

print(mag_list)

for j in range(len(mag_list)):
    for i in range(len(mag_list)-1):
        if mag_list[i] > mag_list[i+1]:
            buffer = mag_list[i+1]
            line_buffer = lines[i+1]
            mag_list[i+1]=mag_list[i]
            lines[i+1] = lines[i]
            mag_list[i] = buffer
            lines[i] = line_buffer

print(lines)