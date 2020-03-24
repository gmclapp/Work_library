import pandas as pd
import Tdms_file_converter as TFC
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib
from matplotlib.lines import Line2D
matplotlib.use("TkAgg")
import tkinter as tk
from tkinter import filedialog
import os

class plot_file:
    def __init__(self):
        self.path = tk.StringVar()
        self.file = tk.StringVar()
        self.file_index = 0
        self.file_list = []

    def next_file_cmd(self):
        if self.file_index < len(self.file_list):
            self.file_index += 1
            self.file.set(self.file_list[self.file_index])
    def prev_file_cmd(self):
        if self.file_index > 0:
            self.file_index -= 1
            self.file.set(self.file_list[self.file_index])
            
    def dir_cmd(self):
        self.file_index = 0
        self.path.set(filedialog.askdirectory())
        
        self.file_list = TFC.tdms_files_in_dir(self.path.get())

class GUI:
    def __init__(self,master):
        frame = tk.Frame(master)
        #master.geometry("600x300") # Width x Height
        frame.pack()

        # Build frames
        self.dir_frame = tk.Frame(frame, border=3, relief=tk.RAISED,bg='blue')
        self.file_frame = tk.Frame(frame, border=3, relief = tk.RAISED,bg='red')
        self.time_frame = tk.Frame(frame, border=3, relief = tk.RAISED)
        self.plot_frame = tk.Frame(frame, border=3, relief = tk.RAISED)

        # Add menubar
        self.menubar = tk.Menu(master)
        
        self.filemenu = tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Set working directory")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit",command=frame.quit)

        self.menubar.add_cascade(label="File",menu=self.filemenu)

        self.helpmenu = tk.Menu(self.menubar,tearoff=0)
        self.helpmenu.add_command(label="About")

        self.menubar.add_cascade(label="Help",menu=self.helpmenu)
        
        master.config(menu=self.menubar)

        # Add plot objects
        self.PlotA = plot_file()
        self.PlotB = plot_file()
        
        # Add buttons
        self.apply_button = tk.Button(self.time_frame,text="Apply",command=self.apply_cmd)
        

        self.next_button = tk.Button(self.file_frame,text=">",command=self.PlotA.next_file_cmd)
        
        self.prev_button = tk.Button(self.file_frame,text="<",command=self.PlotA.prev_file_cmd)  

        ##--- These need to be altered so that the command function can be used by both entry boxes ---##
        self.next_buttonB = tk.Button(self.file_frame,text=">",command=self.PlotB.next_file_cmd)
        
        self.prev_buttonB = tk.Button(self.file_frame,text="<",command=self.PlotB.prev_file_cmd)
        
        self.open_button = tk.Button(self.plot_frame,text="Open",command=self.open_cmd)
        
        # Add text entry fields and askdirectory buttons
        

        self.path_entry = tk.Entry(self.dir_frame,textvariable=self.PlotA.path,width=100)
        
        self.dir_button = tk.Button(self.dir_frame,text="Dir",command=self.PlotA.dir_cmd)
        
        self.current_file_entry = tk.Entry(self.file_frame,textvariable=self.PlotA.file,width=100)

        self.path_entryB = tk.Entry(self.dir_frame,textvariable=self.PlotB.path,width=100)

        self.dir_buttonB = tk.Button(self.dir_frame,text='Dir',command=self.PlotB.dir_cmd)

        self.current_file_entryB = tk.Entry(self.file_frame,textvariable=self.PlotB.file,width=100)

        # Add plot preview
        self.plot_fig, self.ax = plt.subplots(1,1,figsize=(10,6),dpi=100)
        self.ax.set_xlim(25,75)
        self.ax.set_ylim(0,110)
        
        self.canvas = FigureCanvasTkAgg(self.plot_fig,master=self.plot_frame)
        self.canvas.draw()
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.plot_frame)
        self.toolbar.update()

        # Build the GUI
        self.dir_frame.pack()
        self.file_frame.pack()
        self.time_frame.pack()
        self.plot_frame.pack()
        
        self.current_file_entry.grid(row=1,column=0)
        self.dir_button.grid(row=1,column=1)
        self.current_file_entryB.grid(row=3,column=0)
        self.dir_buttonB.grid(row=3,column=1)

        
        self.path_entry.grid(row=0,column=0)
        self.prev_button.grid(row=0,column=1)
        self.next_button.grid(row=0,column=2)

        self.path_entryB.grid(row=2,column=0)
        self.prev_buttonB.grid(row=2,column=1)
        self.next_buttonB.grid(row=2,column=2)

        self.canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        self.apply_button.pack(side=tk.TOP)

        self.open_button.pack(side=tk.LEFT)

    def apply_cmd(self):
        self.full_pathA = os.path.join(self.PlotA.path.get(),self.PlotA.file.get())
        self.full_pathB = os.path.join(self.PlotB.path.get(),self.PlotB.file.get())
        
##        self.full_path = os.path.join(self.path.get(),self.current_file.get())
##        print(self.full_path)
        data = {'transitions':{'P_over':95,
                           'P_to_R':59,
                           'R_to_N':42,
                           'N_to_D':25,
                           'D_to_N':32,
                           'N_to_R':49,
                           'R_to_P':75,
                           'D_over':5,
                           'x_upper':65,
                           'x_lower':35},
            'file':self.full_pathA
            }
        dataB = {'transitions':{'P_over':95,
                           'P_to_R':59,
                           'R_to_N':42,
                           'N_to_D':25,
                           'D_to_N':32,
                           'N_to_R':49,
                           'R_to_P':75,
                           'D_over':5,
                           'x_upper':65,
                           'x_lower':35},
            'file':self.full_pathB
            }
        # re-plot the preview window
        self.ax.clear()
        self.canvas.figure.axes[0] = melexsis_plotter(self.ax, data)
        self.canvas.figure.axes[0] = melexsis_plotter(self.ax, dataB,faded=True)
        
        axis = self.canvas.figure.axes[0]
        axis.set_xlim(25,75)
        axis.set_ylim(0,110)
        
        self.canvas.draw()
    def open_cmd(self):
        data = {'transitions':{'P_over':95,
                           'P_to_R':59,
                           'R_to_N':42,
                           'N_to_D':25,
                           'D_to_N':32,
                           'N_to_R':49,
                           'R_to_P':75,
                           'D_over':5,
                           'x_upper':65,
                           'x_lower':35},
            'file':self.full_path
            }
        melexsis_plotter(self.ax, data)
        plt.show()

def melexsis_plotter(ax, data,faded=False):
    '''takes a matplotlib axis and a data structure as arguments. Plots melexis data to that axis using data
    from the structure.'''
    pd.set_option('display.max_columns',None)
    DF_list = TFC.tdms_to_dfs(data['file'])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim(25, 75)
    ax.set_ylim(0,110)

    CAN_data = DF_list[1][1]

    X = CAN_data['X_AVG'].tolist()
    Y = CAN_data['Y_AVG'].tolist()
    GEAR = CAN_data['Reported Gear']

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

        plot_color = 'green'
        if GEAR[i] == 'Park':
            plot_color = 'green'
        elif GEAR[i] == 'Reverse':
            plot_color = 'blue'
        elif GEAR[i] == 'Neutral':
            plot_color = 'yellow'
        elif GEAR[i] == 'Drive':
            plot_color = 'purple'
        else:
            plot_color = 'red'
        if faded:
            custom_alpha = 0.5
            custom_style = ':'
        else:
            custom_alpha = 1
            custom_style = '-'
        ax.plot(X[i:i+2],
                Y[i:i+2],
                color=plot_color,
                linestyle=custom_style,
                alpha=custom_alpha)
        
        
    ax.hlines(data['transitions']['P_over'],
              data['transitions']['x_lower'],
              data['transitions']['x_upper'],
              'black',
              'solid')
              
    ax.hlines(data['transitions']['P_to_R'],
              data['transitions']['x_lower'],
              data['transitions']['x_upper'],
              'black',
              'solid')
              
    ax.hlines(data['transitions']['R_to_N'],
              data['transitions']['x_lower'],
              data['transitions']['x_upper'],
              'black',
              'solid')
              
    ax.hlines(data['transitions']['N_to_D'],
              data['transitions']['x_lower'],
              data['transitions']['x_upper'],
              'black',
              'solid')

    ax.hlines(data['transitions']['D_to_N'],
              data['transitions']['x_lower'],
              data['transitions']['x_upper'],
              'black',
              'solid')
              
    ax.hlines(data['transitions']['N_to_R'],
              data['transitions']['x_lower'],
              data['transitions']['x_upper'],
              'black',
              'solid')
              
    ax.hlines(data['transitions']['R_to_P'],
              data['transitions']['x_lower'],
              data['transitions']['x_upper'],
              'black',
              'solid')
              
    ax.hlines(data['transitions']['D_over'],
              data['transitions']['x_lower'],
              data['transitions']['x_upper'],
              'black',
              'solid')

    ax.vlines(data['transitions']['x_lower'],
              data['transitions']['P_over'],
              data['transitions']['D_over'],
              'black',
              'solid')
              
    ax.vlines(data['transitions']['x_upper'],
              data['transitions']['P_over'],
              data['transitions']['D_over'],
              'black',
              'solid')

    ax.hlines(y_min,x_min,x_max,'red','dashed')
    ax.hlines(y_max,x_min,x_max,'red','dashed')
    ax.vlines(x_min,y_min,y_max,'red','dashed')
    ax.vlines(x_max,y_min,y_max,'red','dashed')

    ax.scatter(X[0],Y[0],c='r',marker='x') # Plot first point
    ax.scatter(X[-1],Y[-1],c='b',marker='x') # Plot last point

    custom_legend = [Line2D([0],[0],color='green'),
                     Line2D([0],[0],color='blue'),
                     Line2D([0],[0],color='yellow'),
                     Line2D([0],[0],color='purple'),
                     Line2D([0],[0],color='red')]
    
    ax.legend(custom_legend,['Park','Reverse','Neutral','Drive','Error'],
              title='Reported gear')

if __name__ == '__main__':
        
    root = tk.Tk()

    app = GUI(root)
    root.mainloop()
    root.destroy()
