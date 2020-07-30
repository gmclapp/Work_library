import pandas as pd
import Tdms_file_converter as TFC
import matplotlib.pyplot as plt
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

    def build_path(self):
        self.full_path = os.path.join(self.path.get(),self.file.get())
        print(self.full_path)

class GUI:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack()

        # Build frames
        self.dir_frame = tk.Frame(frame, border=3, relief=tk.RAISED,bg='blue')
        self.file_frame = tk.Frame(frame, border=3, relief=tk.RAISED,bg='red')
        
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
        self.Plot = plot_file()
        
        # Add buttons
        self.next_button = tk.Button(self.file_frame,text=">",command=self.Plot.next_file_cmd)     
        self.prev_button = tk.Button(self.file_frame,text="<",command=self.Plot.prev_file_cmd)
        self.apply_button = tk.Button(self.file_frame,text="Apply",command=self.Plot.build_path)
        
        # Add text entry fields and askdirectory buttons
        

        self.path_entry = tk.Entry(self.dir_frame,textvariable=self.Plot.path,width=100)        
        self.dir_button = tk.Button(self.dir_frame,text="Dir",command=self.Plot.dir_cmd)
        self.current_file_entry = tk.Entry(self.file_frame,textvariable=self.Plot.file,width=100)
        
        # Build the GUI
        self.dir_frame.pack()
        self.file_frame.pack()

        self.path_entry.pack(side=tk.LEFT)
        self.dir_button.pack(side=tk.LEFT)
        self.current_file_entry.pack(side=tk.LEFT)
        self.prev_button.pack(side=tk.LEFT)
        self.next_button.pack(side=tk.LEFT)
        self.apply_button.pack(side=tk.TOP)
        
if __name__ == '__main__':

    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
    root.destroy()
