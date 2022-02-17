# Import the necessary libraries
import sys
import pandas as pd

# Defining my function
def crop_file():
    try:
        # Opening the csv file as a dataframe in pandas
        df = pd.read_csv('bristol-air-quality-data.csv', delimiter=';', low_memory=False)

        # Selecting the datetime column and changing the datatype to datetime using pandas datetime function
        df['Date Time'] = pd.to_datetime(df['Date Time'])

        # Removing all the rows where the values were taken before the 1st of January 2010.
        df = df.loc[df['Date Time'] >= '2010-01-01T00:00:00+00:00']

        # Converting the dataframe back to a csv file.
        return df.to_csv('crop.csv', index=False)

    except BaseException as err:
        print(f"An error occurred: {err}")
        sys.exit(1)


crop_file()
