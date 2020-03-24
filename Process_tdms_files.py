import Tdms_file_converter as TFC
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
import csv

class plot_file:
    def __init__(self):
        self.path = tk.StringVar()
        self.file = tk.StringVar()
        self.file_index = 0
        self.file_list = []
        self.output = [["Filename","Warrant","Sample","Starting X","Starting Y",
                  "Ending X","Ending Y","Min X","Max X","Min Y","Max Y",
                   "P to R","R to N","N to D","D to N","N to R","R to P"]]

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

    def start_cmd(self):
        self.file_list = TFC.tdms_files_in_dir(self.path.get())
        for f in self.file_list:
            self.get_parameters(f)

        with open(os.path.join(self.path.get(),"output.csv"),"a",newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.output)

    def get_parameters(self,f):
        full = os.path.join(self.path.get(),f)
        curr_fileDFS = TFC.tdms_to_dfs(full)
        metaDF = curr_fileDFS[0][1]
        DataDF = curr_fileDFS[1][1]
        
        warrant = metaDF.loc[metaDF.Name == "Warrant Number","Value"].values[0]
        sample = metaDF.loc[metaDF.Name == "Sample Number","Value"].values[0]
##        print("Warrant: {}\nSample:{}".format(warrant,sample))

        # Process X_avg data
        X_data = DataDF["X_AVG"].tolist()
        X_data = list(filter(lambda a: a != 0,X_data))
        X_data = list(filter(lambda a: a != 131.07,X_data))
        
        if len(X_data) != 0:
            X_start = X_data[0]
            X_end = X_data[-1]
            X_min = min(X_data)
            X_max = max(X_data)
##            print("Min X: {}\nMax X: {}\nStart X: {}\nEnd X: {}".format(X_min,
##                                                                X_max,
##                                                                X_start,
##                                                                X_end))
        else:
            print("{} Does not have any data!".format(sample))

        # Process Y_avg data
        Y_data = DataDF["Y_AVG"].tolist()
        Y_data = list(filter(lambda a: a != 0,Y_data))
        Y_data = list(filter(lambda a: a != 131.07,Y_data))

        if len(Y_data) != 0:
            Y_start = Y_data[0]
            Y_end = Y_data[-1]
            Y_min = min(Y_data)
            Y_max = max(Y_data)
##            print("Min Y: {}\nMax Y: {}\nStart Y: {}\nEnd Y: {}".format(Y_min,
##                                                                Y_max,
##                                                                Y_start,
##                                                                Y_end))
        else:
            print("{} Does not have any data!".format(sample))
        
        Gear_data = DataDF["Reported Gear"]

        # Separate data into series by reported gear position
        Park = DataDF.loc[DataDF["Reported Gear"]=="Park","Extension [mm]"]
        Reverse = DataDF.loc[DataDF["Reported Gear"]=="Reverse","Extension [mm]"]
        Neutral = DataDF.loc[DataDF["Reported Gear"]=="Neutral","Extension [mm]"]
        Drive = DataDF.loc[DataDF["Reported Gear"]=="Drive","Extension [mm]"]

        # Get gear transitions
        PtoR = Reverse.tolist()[0]
        RtoN = Neutral.tolist()[0]
        NtoD = Drive.tolist()[0]

        DtoN = Drive.tolist()[-1]
        NtoR = Neutral.tolist()[-1]
        RtoP = Reverse.tolist()[-1]
        
##        print("Park to Reverse: {}".format(PtoR))
##        print("Reverse to Neutral: {}".format(RtoN))
##        print("Neutral to Drive: {}".format(NtoD))
##
##        print("Drive to Neutral: {}".format(DtoN))
##        print("Neutral to Reverse: {}".format(NtoR))
##        print("Reverse to Park: {}".format(RtoP))

        try:
            self.output.append([f,warrant,sample,X_start,Y_start,
                           X_end,Y_end,X_min,X_max,Y_min,Y_max,
                           PtoR,RtoN,NtoD,DtoN,NtoR,RtoP])
        except:
            print("Error!")
            
class GUI:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack()

        work_dir = plot_file()
        self.path_entry = tk.Entry(frame,textvariable=work_dir.path,width=100)
        
        self.dir_button = tk.Button(frame,text="Dir",
                                    command=work_dir.dir_cmd)
        self.start_button = tk.Button(frame,text="Start",
                                      command=work_dir.start_cmd)

        frame.pack()
        self.path_entry.pack()
        self.dir_button.pack()
        self.start_button.pack()


    
if __name__ == '__main__':
        
    root = tk.Tk()

    app = GUI(root)
    pd.set_option('display.max_columns',None)
    root.mainloop()
    
    root.destroy()
