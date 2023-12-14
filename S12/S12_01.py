import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

ID = "1005497"

# ------------------------------ RETRIEVING DATA ----------------------------- #
with open(f"./S12/{ID}.dat", "r") as f:
    lines = f.readlines()

mjd_offset = 52000
data_mjd = []
data_mag = []
data_err = []

lines = lines[20:]
for line in lines:
    line = line.strip()
    mjd, mag, err = line.split()
    data_mag.append(float(mag))
    data_mjd.append(float(mjd) - mjd_offset)
    data_err.append(float(err))

# --------------------------------- CONSTANTS -------------------------------- #
period_min_min = 10.0
period_min_day = period_min_min / (60.0 * 24.0)
period_max_min = 1500.0
period_max_day = period_max_min / (60.0 * 24.0)
step_min = 0.1
step_day = step_min / (60.0 * 24.0)
n_bins = 10

# ------------------------------- PERIOD SEARCH ------------------------------ #
period_day = period_min_day
data_per = []
data_var = []

while period_day < period_max_day:
    data_phase = [(mjd / period_day - int(mjd / period_day)) for mjd in data_mjd]

    total_variance = 0.0

    for i in range(n_bins):
        bin_min = i / n_bins
        bin_max = (i + 1) / n_bins
        data_bin = [data_mag[j] for j in range(len(data_phase)) if bin_min <= data_phase[j] < bin_max]

        if not data_bin:
            continue

        variance_in_bin = np.var(data_bin)
        total_variance += variance_in_bin

    data_per.append(period_day * 24.0)
    data_var.append(total_variance)
    period_day += step_day

# ------------------------------- PLOTTING ----------------------------------- #
fig = Figure()
canvas = FigureCanvasAgg(fig)
ax2 = fig.add_subplot(111)

ax2.set_xlabel('Period [hr]')
ax2.set_ylabel('Variance')

ax2.set_xlim (15, 17)

ax2.plot(data_per, data_var, linestyle='-', color='blue', linewidth=3, label='Result of PDM analysis')
ax2.legend()

fig.savefig(f"./S12/S12_01_zoom1.png", dpi=150)

fig.clf()

ax = fig.add_subplot(111)

ax.set_xlabel ('Phase')
ax.set_ylabel ('Apparent Magnitude [mag]')

ax.invert_yaxis ()
ax.errorbar (data_phase, data_mag, yerr=data_err, linestyle='None', marker='o', markersize=5, color='green', ecolor='black', capsize=5, label='folded lightcurve')

fig.savefig(f"./S12/S12_01_error.png", dpi=150)
