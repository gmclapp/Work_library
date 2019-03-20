import misc_functions as mf
import pandas as pd
import time

def detect_step(df, X, Y,edge="Falling", step_size=1):
    '''Detects a step shape in 2D data contained in dataframe df. step_size is
    the minimum detectable step size. Steps are defined by a change in polarity
    of the first derivative of the supplied x-y data.

    edge can be used to detect either the Falling or the Rising edge of a slope
    polarity change.

    Returns a list of (x,y) pairs corresponding to the edges of detected
    steps.'''
    mf.dxdy(df,Y,X)
    log("Appending first derivative column")
    slope = 0
    edges = []
    for i,elem in enumerate(df["dx/dy"]):
        test = slope/float(df.at[i,"dx/dy"])

        if test < 0 and slope > 0 and edge=="Falling":
            edges.append((df.at[i,X],df.at[i,Y]))
            log("Slope polarity change. Falling edge")
        elif test < 0 and slope < 0 and edge == "Rising":
            edges.append((df.at[i,X],df.at[i,Y]))
            log("Slope polarity change. Rising edge")
        slope = float(df.at[i,"dx/dy"])

    return(edges)

def log(this):
    log=open("log.txt",mode='a')
    print(mf.timestamp(),this,file=log)
    log.close()
    
def main(directory=None, X=None, Y=None, edge="Falling"):
    '''If used as a sub-routine, directory should include the filename. Pass
    a path complete with filename to find rising or falling edges in x-y
    data.'''
    
    if directory == None:
        directory = input("Enter directory\n>>>")
        log("User entered directory \""+directory+"\"")
        f = input("Enter file name\n>>>")
        log("User entered filename \""+f+"\"")
        X='Extension (mm)'
        Y='Primary load measurement (N)'
        edge="Falling"
        
        filename = directory+f
    else:
        filename = directory
    try:
        df = pd.read_csv(filename)
        edges = detect_step(df,X,Y,edge)
        return(edges)

    except FileNotFoundError:
        log("Bad filename given")
        time.sleep(15)

if __name__ == '__main__':
    main()
