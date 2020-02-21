import matplotlib.pyplot as plt
import numpy as np

# Specification of cross-over load is 7N +/- 4N
Figure, axes = plt.subplots(1,1,figsize=(6,6))
axes.set_xlabel("Angular displacement from Park ($deg$)")
axes.set_ylabel("")
axes.set_ylim([-3,3])


low_limit = float(input("Enter lower limit (deg)"))
nominal = float(input("Enter nominal attribute value (deg)"))
high_limit = float(input("Enter upper limit (deg)"))

ambient = float(input("Enter the average measurement at ambient temperature (deg)"))
hot = float(input("Enter the average measurement at hot temperature (deg)"))
cold = float(input("Enter the average measurement at cold temperature (deg)"))
ambient2 = float(input("Enter the average measurement once returned to ambient ambient temperature (deg)"))

lower_x = min(low_limit,ambient,hot,cold)-0.5
upper_x = max(high_limit,ambient,hot,cold)+1.35

axes.set_xlim([lower_x,upper_x])
# Set tick mark sizes
size = 0.25
axis = 0
top = axis + size/2
bot = axis - size/2

# Plot Limits
axes.vlines(low_limit,bot,top,'black','solid')
axes.vlines(high_limit,bot,top,'black','solid')
axes.vlines(nominal,bot,top,'black','solid')
axes.hlines(0,low_limit,high_limit,'black','solid')

# Plot labels
axes.annotate(s=str(low_limit),xy=(low_limit,axis-(size+0.1)),horizontalalignment='center')
axes.annotate(s=str(nominal),xy=(nominal,axis-(size+0.1)),horizontalalignment='center')
axes.annotate(s=str(high_limit),xy=(high_limit,axis-(size+0.1)),horizontalalignment='center')

# Plot measurements
axes.plot(ambient,axis,marker='o',color='red')
axes.plot(hot,axis,marker='o',color='red')
axes.plot(cold,axis,marker='o',color='red')
axes.plot(ambient2,axis,marker='o',color='red')

# Hide tick labels
axes.get_xaxis().set_ticks([])
axes.get_yaxis().set_ticks([])

# Annotation arrows
ambient_string = 'Ambient; ' + str(ambient)
hot_string = 'Hot; ' + str(hot)
cold_string = 'Cold; ' + str(cold)
ambient2_string = 'Final ambient; ' + str(ambient2)

axes.annotate(s=ambient_string,xy=(ambient,axis),xytext=(ambient+0.5,axis+1),arrowprops=dict(arrowstyle='->'))
axes.annotate(s=hot_string,xy=(hot,axis),xytext=(hot+0.5,axis+1),arrowprops=dict(arrowstyle='->'))
axes.annotate(s=cold_string,xy=(cold,axis),xytext=(cold+0.5,axis-1),arrowprops=dict(arrowstyle='->'))
axes.annotate(s=ambient2_string,xy=(ambient2,axis),xytext=(ambient2+0.25,axis+1.5),arrowprops=dict(arrowstyle='->'))

plt.show()
