from operator import index
import numpy as np
import astropy.timeseries as timeseries
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

# ------------------------------ RETRIEVING DATA ----------------------------- #
hdul = fits.open("./S12/klpr2.fits")

lc = hdul['LIGHTCURVE'].data
data_mjd = lc['TIME']
data_mag = lc['MAG']

trial = 169.37/24
data_phase = np.array([])

#     phase = (float(mjd) - data_mjd[0])/trial
#     phase -= int(phase)
#     data_phase = np.append(data_phase, phase)

freqs, powers = timeseries.LombScargle(data_mjd, data_mag).autopower()

data_per_hr = []
data_power = []
for freq, power in zip(freqs,powers):
    data_per_hr.append(1/freq*24)
    data_power.append(power)

maximum = data_per_hr[data_power.index(max(data_power))]
print(maximum)
per_min_hr = maximum - 3
per_max_hr = maximum + 3

# ------------------------------- PLOTTING DATA ------------------------------ #
fig = Figure()
canvas = FigureCanvasAgg(fig)
ax = fig.add_subplot(111)

ax.plot (data_per_hr, data_power, linestyle='-', linewidth=3, color='blue', label='result of Lomb-Scargle periodogram')

ax.legend()
fig.savefig("./S12/S12_02_lomb")

# -------------------------------- ZOOMING IN -------------------------------- #
# fig.clf()
# ax = fig.add_subplot(111)
# ax.set_xlim(per_min_hr, per_max_hr)
# ax.plot (data_per_hr, data_power, linestyle='-', linewidth=3, color='blue', label='Lomb-Scargle periodogram')
# ax.legend()
# fig.savefig("./S12/S12_02_lomb_zoom")


# # ---------------------------------- FOLDING --------------------------------- #
# fig.clf()
# ax = fig.add_subplot (111)
# ax.set_xlabel ('Phase')
# ax.set_ylabel ('Magnitude [mag]')
# ax.invert_yaxis ()
# label = f"folded lightcurve constructed from $P = {trial * 24.0:6.4f}$ hr"
# ax.errorbar (data_phase, data_mag, yerr=data_err, \
# linestyle='None', marker='.', markersize=5, color='blue', ecolor='black', capsize=0, label=label)
# ax.errorbar (data_phase + 1.0, data_mag, yerr=data_err, linestyle='None', marker='.', markersize=5, color='blue', ecolor='black', capsize=0)
# ax.legend (bbox_to_anchor=(1.0, 1.12), loc='upper right')
# fig.savefig ("./S12/S12_02_folded", dpi=150)