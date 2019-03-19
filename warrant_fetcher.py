import os
import misc_functions as mf # Uses 0.2.5
import csv

__version__ = "0.0.1"

def fetch_warrant_paths():
    rfile="warrants.csv"
    RDR = csv.reader(open(rfile))
    data_dir = "Parametric Data"
    sep="\\"
    log = open("log.txt", mode='a')

    warrants = []
    for row in RDR:
        warrants.append(int(row[0]))

    good,bad = mf.gen_warrant_links(warrants)

    paths = []
    print("{} Good links".format(mf.timestamp()),file=log)
    for g in good:
        sub_dir = mf.similar_dir(g,data_dir,0.5)
        if not sub_dir == None:
            path = sep.join([g,sub_dir])
            if os.path.isdir(path):
                paths.append(sep.join([g,sub_dir]))
            else:
                print("{} {} is not a directory.".format(mf.timestamp(),
                                                         path),
                      file=log)
        else:
            print("{} Parametric data folder not found in {}.".format(mf.timestamp(),
                                                                      g),
                  file=log)
            bad.append(g)
        
    print("\n{} Bad links".format(mf.timestamp()),file=log)
    for b in bad:
        print("{} {}".format(mf.timestamp(),b),file=log)

    log.close()
    return(paths)

    
