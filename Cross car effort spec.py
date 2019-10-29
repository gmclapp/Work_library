import matplotlib.pyplot as plt
import numpy as np

# Specification of cross-over load is 7N +/- 4N
theta = [0, 7.5, 7.8, 8,8.1, 8.2]
F = [5, 9.5, 10, 11, 12, 24]

Figure, axes = plt.subplots(1,1,figsize=(6,6))
axes.set_xlabel("Cross-over angle ($deg$)")
axes.set_ylabel("Cross-over effort (N)")
axes.plot(theta,F, 'r-')

# Plot Overtravel contact
axes.vlines(7.8,0,24,'blue','dotted')

# Plot max effort measurement location
axes.vlines(7, 0, 24,'blue','dashed')

# Hide tick labels
axes.get_xaxis().set_ticks([])
axes.get_yaxis().set_ticks([])

axes.legend(("Cross-over effort","End travel stop","Maximum cross-over effort"))
axes.annotate(s='',xy=(7,2),xytext=(7.8,2),arrowprops=dict(arrowstyle='<->'))
axes.annotate(s='0.5 \ndeg',xy=(7.1,2.5))
plt.show()
