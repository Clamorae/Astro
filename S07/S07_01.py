import astropy.units as unit

length = 100 * unit.micron

print(f"The wavelength of {length} is equal to a frequence of {length.to(unit.Hz,equivalencies= unit.spectral())} or {length.to(unit.GHz,equivalencies= unit.spectral())}")