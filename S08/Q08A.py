with open("./Astro/S08/data.txt","r") as f:
    lines = f.readlines()

store = []
counted = []
for line in lines:
    store.append(line.split()[0])

for word in store:
    if word not in counted:
        print(f"the word {word} appear in the table {store.count(word)} times")
        counted.append(word)