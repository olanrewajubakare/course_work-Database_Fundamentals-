# Importing the necessary libraries
import pandas as pd
import sys

try:
    # Select the date columns in the csv file
    date_cols = ['Date Time', 'DateStart', 'DateEnd']

    # Read the csv file as a dataframe and parse the date columns as dates
    df = pd.read_csv('clean.csv', parse_dates=date_cols)

    # Drop the location and geo_point_2d columns 
    df.drop(['Location', 'geo_point_2d'], axis=1, inplace=True)


    # Intiate an sql with an insert header 
    sql = "INSERT INTO `readings` VALUES\n"

    count = 1

    # Loop through each row of the first 100 values in the dataframe
    for index, row in df.iloc[:100].iterrows():
        # Convert the items of each column in each row to a string
        readings = ["'" + str(x) + "'" for x in row]

        # Join the items and seperate them by commas
        readings = ",".join(readings)

        # Pandas converts missing values to nan, so, replace nan values with null.
        readings =  readings.replace("'nan'", " NULL")

        # Missing date values are converted to NaT, so, replace NaT with null. 
        readings =  readings.replace("'NaT'", " NULL")

        # Add space to True
        readings = readings.replace("'True'", " True")
        # Add space to false
        readings = readings.replace("'False'", " False")

        # Add the readings and a counter to the sql string 
        sql +='(' + str(count) + ', ' + readings + '),' + '\n'
        # Increase the counter by 1 each time we loop through a value
        count += 1

    # Replace the comma and the newline with a semicolon
    new_sql = sql[:-2] + ';'

    # Save the file as insert-100.sql
    file = open("insert.sql", 'w')
    file.write(new_sql + "\n")
    print(new_sql)

except BaseException as err:
    print(f"An error occurred: {err}")
    sys.exit(1)
