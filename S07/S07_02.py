import astropy.time as time

start = time.Time("1901-01-01 12:00:00",format="iso",scale="utc")
end = time.Time("2001-01-01 12:00:00",format="iso",scale="utc")

print(f"There are {end-start} days between {start} and {end}")