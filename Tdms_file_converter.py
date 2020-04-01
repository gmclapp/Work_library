import pandas as pd
import numpy as np
import nptdms 
import csv
import os



def tdms_to_dfs(file_path):
    '''Accepts a path to a *.tdms file as an input and creates a list of
    tuples where the first element in each tuple is a channel name, and the
    second is a pandas data frame with data from that channel.'''
    
    f = nptdms.TdmsFile(file_path)
    
    channels = f.groups() # get channel names
    DF_list = [] # initialize list to store dataframes
    for c in channels:
        new_DF = f.object(c).as_dataframe()
        DF_list.append((c,new_DF))
    
    return(DF_list)

def dfs_to_excel(DF_list, out_file_name):
    '''Accepts a list of tuples where the first element is a sheet name and the
    second is a pandas data frame, and outputs an excel file where each
    dataframe is made a tab in the excel file with the name given.'''
    
    with pd.ExcelWriter(out_file_name+'.xlsx') as writer:
        for df in DF_list:
            df[1].to_excel(writer,df[0])

def tdms_files_in_dir(file_path):
    '''Takes a file path and returns a list of file names with the extension
    *.tdms'''

    tdms_files = []
    for file in os.listdir(file_path):
        if file.endswith(".tdms"):
##            tdms_files.append(os.path.join(file_path,file))
            tdms_files.append(file)

    return(tdms_files)

if __name__ == '__main__':
    working_dir = r'E:\Work\GHSP\HDrive\WIP\12504 - LD Pursuit\Issue #314 - Pursuit DV\Issue #314.5 - DVPV-124 Sensor drift\202000562 vs 202000564 - shimmed part\562'
    file_list = tdms_files_in_dir(working_dir)
    for f in file_list:
        DF_list = tdms_to_dfs(os.path.join(working_dir,f))
        print(f[:-5])
        dfs_to_excel(DF_list, f[:-5])
                      
##    DF_list = tdms_to_dfs(r'E:\Work\GHSP\HDrive\WIP\12504 - LD Police IP shifter\Issue #314 - Pursuit design validation testing\Issue #314.5 - DVPV-124 Sensor drift at 40 and -85C\202000435 - Pivot support test\202000435 Generic Loading.is_ccyclic_RawData\S0007167_Rearward Loading 222N_N_A_20200227131547.tdms')
##    dfs_to_excel(DF_list)
