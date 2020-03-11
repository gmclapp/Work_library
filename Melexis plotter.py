import pandas as pd
import Tdms_file_converter as TFC
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
DF_list = TFC.tdms_to_dfs(r'E:\Work\GHSP\HDrive\WIP\12504 - LD Police IP shifter\Issue #314 - Pursuit design validation testing\Issue #314.5 - DVPV-124 Sensor drift at 40 and -85C\202000529 - Gate trace study\Test Data\202000529/S0007340_Setup 13 - Park_Park_20200310121955.tdms')

fig, ax = plt.subplots(1,1,figsize=(6,6))
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Define gear transitions
P_over = 95
P_to_R = 59
R_to_N = 42
N_to_D = 25

D_to_N = 32
N_to_R = 49
R_to_P = 75
D_over = 5

CAN_data = DF_list[1][1]

X = CAN_data['X_AVG'].tolist()
Y = CAN_data['Y_AVG'].tolist()

X = list(filter(lambda a: a != 0,X))
X = list(filter(lambda a: a != 131.07,X))

Y = list(filter(lambda a: a != 0,Y))
Y = list(filter(lambda a: a != 131.07,Y))


##CAN_data.plot(kind='scatter',x='X1',y='Y1',alpha=1)
x_min = X[0]
y_min = Y[0]
x_max = X[0]
y_max = Y[0]

for i in range(len(X)):
    x_min = min(x_min,float(X[i]))
    x_max = max(x_max,float(X[i]))
    y_min = min(y_min,float(Y[i]))
    y_max = max(y_max,float(Y[i]))
    
    ax.plot(X[i:i+2],Y[i:i+2],color='black')
    
##ax.plot(X,Y)
ax.hlines(P_over,35,65,'black','solid')
ax.hlines(P_to_R,35,65,'black','solid')
ax.hlines(R_to_N,35,65,'black','solid')
ax.hlines(N_to_D,35,65,'black','solid')

ax.hlines(D_to_N,35,65,'black','solid')
ax.hlines(N_to_R,35,65,'black','solid')
ax.hlines(R_to_P,35,65,'black','solid')
ax.hlines(D_over,35,65,'black','solid')

ax.vlines(35,P_over,D_over,'black','solid')
ax.vlines(65,P_over,D_over,'black','solid')

ax.hlines(y_min,x_min,x_max,'red','dashed')
ax.hlines(y_max,x_min,x_max,'red','dashed')
ax.vlines(x_min,y_min,y_max,'red','dashed')
ax.vlines(x_max,y_min,y_max,'red','dashed')

ax.scatter(X[0],Y[0],c='r',marker='x') # Plot first point
ax.scatter(X[-1],Y[-1],c='b',marker='x') # Plot last point

plt.show()
print(CAN_data.head())

