# Import the necessary libraries
import sys
import pandas as pd

# Defining my function
def filter_empty_and_mismatched_siteID():
    try:

        df = pd.read_csv('crop.csv', low_memory=False)
        # Creating a dictionary of where the SiteID is the keys and the LocationID is the values
        d = {
            188: 'AURN Bristol Centre',
            203: 'Brislington Depot',
            206: 'Rupert Street',
            209: 'IKEA M32',
            213: 'Old Market',
            215: 'Parson Street School',
            228: 'Temple Meads Station',
            270: 'Wells Road',
            271: 'Trailer Portway P&R',
            375: 'Newfoundland Road Police Station',
            395: "Shiner's Garage",
            452: 'AURN St Pauls',
            447: 'Bath Road',
            459: 'Cheltenham Road \ Station Road',
            463: 'Fishponds Road',
            481: 'CREATE Centre Roof',
            500: 'Temple Way',
            501: 'Colston Avenue'
        }
        # Creating a variable called df2 that will hold a copy of the original dataframe.
        df2 = df.copy()
        for key, value in d.items():

            # Drop all values in df2 where siteid and locations are correctly matched. Hence, only the mismatched
            # values will remain in df2
            df2 = df2[~((df2['SiteID'] == key) & (df2['Location'] == value))]

        # Printing the line number of the dropped values.
        print('The number of mismatches found and lines removed is', len(df2))

        # Comparing df2 to df on their index. Since df2 only holds mismatched values, all that needs to be done is to
        # drop all df2 in df.
        df = df[~df.index.isin(df2.index)]
        # Converting the filtered records to csv.
        df.to_csv("clean.csv", index=False)

    except BaseException as err:
        print(f"An error occurred: {err}")
        sys.exit(1)


filter_empty_and_mismatched_siteID()
