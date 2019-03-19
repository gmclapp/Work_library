import pandas as pd
import os
import datetime as dt
import time
import csv
import misc_functions as mf
import warrant_fetcher as wf

__version__ = "0.0.1"

def Mikes(testPlan):
    '''Takes the test plan number as an argument and returns links to warrants.
    '''

    print("Looking for DVPR sheet")
    testDict = mf.tab_dict(r'\\jsjcorp.com\data\GHSP\GH\webdata\DVPR\\'\
                        +testPlan+ r'\Update\2590 JL PV Update 1-25-19.xlsx')
    if not testDict is None:
        print("Collecting warrants.")
        warrants = get_Mwarrant_nums(testDict[testPlan])
        print("Testing warrant links.")
        warrants, broken_links = gen_warrant_links(warrants)
        print("Found {} warrants.".format(len(warrants)))
        print("{} broken links".format(len(broken_links)))
        for b in broken_links:
            print(b)
    else:
        print("DVPR not found.")

def get_Mwarrant_nums(xlsxTab):
    '''This function takes a pandas dataframe, probably a tab from tab_dict,
    and extracts a list of warrants from the "Warrant Number" column. This
    function is built to work with Mike Doerr's eDVP&R spreadsheet.'''
    series = xlsxTab["Unnamed: 14"]
    warrants = []
    for i in series:
        if isinstance(i,(int, float)) and not math.isnan(i) and len(str(i)) == 8:
            warrants.append(i)
    return(warrants)

def gen_warrant_links(warrants):
    '''This function takes a list of warrants and builds network links to those
    warrants. the list of warrants must be integers'''
    cur_year = str(dt.date.today().year)
    
    links = []
    broken_links = []
    for w in warrants:
        if cur_year == str(w)[:4]:
            #print("Warrant was this year")
            path = '\\\\jsjcorp.com\\data\\GHSP\\GH\\webdata\\Testing\\' +str(w)
##            path = 'Test warrants\\' +str(w)
        else:
            #print("Warrant was not this year")
            path = '\\\\jsjcorp.com\\data\\GHSP\\GH\\webdata\\Testing\\' +str(w)[:4]+'\\'+str(w)
##            path = 'Test warrants\\' +str(w)[:4]+'\\'+str(w)
        if os.path.exists(path):
            links.append(path)
        else:
            broken_links.append(path)

    return(links, broken_links)

def parametric_eval(warrant_link):
    '''This function takes a link to a warrant folder, and evaluates the
    parametric stand data contained therein.'''
    meas_val_header = "Unnamed: 6"
    lower_spec_header = "Unnamed: 5"
    upper_spec_header = "Unnamed: 7"
    attribute_label_header = "Unnamed: 9"
    
    folder = warrant_link + r'\Parametric Data'
    for filename in os.listdir(folder):
        if filename.endswith(".xlsx"):
            xlsx = pd.ExcelFile(folder+'\\'+filename)
            Sheet_frames = {sh:xlsx.parse(sh) for sh in xlsx.sheet_names}
            for i, element in enumerate(Sheet_frames["EVAL_PARAM_SUM"][meas_val_header]):
                lower = Sheet_frames["EVAL_PARAM_SUM"][lower_spec_header][i]
                upper = Sheet_frames["EVAL_PARAM_SUM"][upper_spec_header][i]
                try:
                    if (lower <= element <= upper and
                        str(element) != ""):
                        print(Sheet_frames["EVAL_PARAM_SUM"][attribute_label_header][i],
                              " = Pass")
                    else:
                        print(Sheet_frames["EVAL_PARAM_SUM"][attribute_label_header][i],
                              " = Fail")
                except TypeError:
                    if str(element) == "0x00":
                        pass
                    elif str(element) == "0x40":
                        print(Sheet_frames["EVAL_PARAM_SUM"][attribute_label_header][i],
                              ":",element,"Test not complete this cycle",sep='')
                    elif str(element) == "0x50":
                        print(Sheet_frames["EVAL_PARAM_SUM"][attribute_label_header][i],
                              ":",element,
                              "Test not complete this cycle\n",
                              "Test not complete since last clear.",
                              sep='')
                    else:
                        pass
        else:
            continue


#----Main---#
log = open("log.txt", mode='a')
paths = wf.fetch_warrant_paths() 
for p in paths:
    log = open("log.txt", mode='a')
    print("\n{} Processing {} On response time.".format(mf.timestamp(),
                                                      p),file=log)
    log.close()
    Solenoid_on_response.main(p)

    log = open("log.txt", mode='a')
    print("\n{} Processing {} Off response time.".format(mf.timestamp(),
                                                       p),
          file=log)
    log.close()
    Solenoid_off_response.main(p)
