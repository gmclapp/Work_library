import pandas as pd
import numpy as np
import nptdms 
import csv
import pip



def tdms_to_dfs(file_path):
    '''Accepts a path to a *.tdms file as an input and creates a list of pandas
    data frames with that file. Where each channel in the tdms file is a
    separate dataframe.'''
    
    f = nptdms.TdmsFile(file_path)
    
    channels = f.groups() # get channel names
    DF_list = [] # initialize list to store dataframes
    for c in channels:
        new_DF = f.object(c).as_dataframe()
        DF_list.append(new_DF)
    
    return(DF_list)

def dfs_to_excel(DF_list):
    '''Accepts a list of pandas data frames and outputs an excel file where each
    dataframe is made a tab in the excel file.'''
    with pd.ExcelWriter('output.xlsx') as writer:
        for i, df in enumerate(DF_list):
            df.to_excel(writer,sheet_name=str(i))

if __name__ == '__main__':
    pip.install('openpyxl')
    DF_list = tdms_to_dfs(r'E:\Work\GHSP\HDrive\WIP\12504 - LD Police IP shifter\Issue #314 - Pursuit design validation testing\Issue #314.5 - DVPV-124 Sensor drift at 40 and -85C\202000435 - Pivot support test\202000435 Generic Loading.is_ccyclic_RawData\S0007167_Rearward Loading 222N_N_A_20200227131547.tdms')
    dfs_to_excel(DF_list)
