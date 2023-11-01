import requests

response = requests.get("https://s3b.astro.ncu.edu.tw/ai_202309/data/q07.data")

splitted = response.content.split(b"\n")
counted = []

for word in splitted:
    if word not in counted:
        print(f"the word {word} appear in the table {splitted.count(word)} times")
        counted.append(word)