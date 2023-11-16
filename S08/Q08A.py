with open("./Astro/S08/data.txt","r") as f:
    lines = f.readlines()

store = []
counted = []
for word in lines:
    if word not in counted:
        print(f"the word {word[:-1]} appear in the table {lines.count(word)} times")
        counted.append(word)
