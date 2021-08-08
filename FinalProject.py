import pandas as pd
# To install 'pandas' library:
# $>  pip install pandas
# Pip is a python-based library installer.

# FinalProject.py 2021 by Sean Cox
# Created for IOT Security
if __name__ == '__main__':

    # Read input csv into a pandas DataFrame which will make data manipulation more simple.
    df = pd.read_csv('project_input.csv')

    # Now we initialize a conflict counter, iterate all rows of input, and count conflicts when they occur.
    conflict_count = 0
    for i in range(len(df)):
        Motion1 = df.iloc[i, 0]
        Motion2 = df.iloc[i, 1]
        Light1  = df.iloc[i, 2]
        DrivewayCam = df.iloc[i, 3]
        PorchCam = df.iloc[i, 4]
        PorchLight = df.iloc[i, 5]
        if Motion1 != 0 and Motion2 != 0 or DrivewayCam != 0 and PorchCam != 0:
            if Motion1 == Motion2:
                print("Motion1 = ", Motion1, "| Motion2 = ", Motion2)
                conflict_count += 1
            if DrivewayCam == PorchCam:
                print("DrivewayCam = ", DrivewayCam, "| PorchCam = ", PorchCam)
                conflict_count += 1
    print("Total Conflicts Encountered: ", conflict_count)



