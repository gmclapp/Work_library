import misc_functions as mf
import pandas as pd

def detect_step(df, X, Y, step_size=1,edge="Falling"):
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
        
        #print("Test metric: {} Next slope: {}".format(test, slope))
        if test < 0 and slope > 0 and edge=="Falling":
            edges.append((df.at[i,X],df.at[i,Y]))
            log("Slope polarity change. Falling edge")
        elif test < 0 and slope < 0 and edge == "Rising":
            edges.append((df.at[i,X],df.at[i,Y]))
            log("Slope polarity change. Rising edge")
        slope = float(df.at[i,"dx/dy"])

    print(df.head(20))
    return(edges)

def log(this):
    log=open("log.txt",mode='a')
    print(mf.timestamp(),this,file=log)
    log.close()
    
def main(directory=None):
    if directory == None:
        directory = input("Enter directory\n>>>")
        log("User entered directory \""+directory+"\"")
        f = input("Enter file name\n>>>")
        log("User entered filename \""+f+"\"")
        
    filename = directory+f
    try:
        df = pd.read_csv(filename)
        edges = detect_step(df,
                            'Extension (mm)',
                            'Primary load measurement (N)'
                            ,edge="Falling")
        print(edges)
    except FileNotFoundError:
        log("Bad filename given")

if __name__ == '__main__':
    main()
