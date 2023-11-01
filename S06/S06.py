import requests

with open("./Astro/S06/data.txt","w") as f:
    f.write(requests.get("http://elysium.elte.hu/~dalyag/GLADE+.txt").content)