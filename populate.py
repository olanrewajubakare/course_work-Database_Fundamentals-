# module imports
import mariadb
import sys
import csv

#
try:
    # Setting the username and the password and then connecting to mariadb
    conn = mariadb.connect(
        user='root',
        password='',
        host='127.0.0.1',
        port=3306,
    )
    # Printing Connection to be sure that it works
    print(conn)
    cur = conn.cursor()
    # Creating the database and dropping anyone that has the same name as the one I am about to create
    cur.execute('DROP DATABASE IF EXISTS `pollution-db2`')
    cur.execute('CREATE DATABASE `pollution-db2`')

    # Creating at empty records list
    records = []

    # Specifying the database to be used or setting a database handle
    cur.execute("USE `pollution-db2`")
    # SQL Query to create the necessary tables
    stations_sql = """CREATE TABLE IF NOT EXISTS `stations`
    (`Stationid` INT(11) NOT NULL, 
    `Location` text NOT NULL,
    `geo_point_2d` VARCHAR(40) NOT NULL,
    PRIMARY KEY(`Stationid`));"""

    readings_sql = """CREATE TABLE IF NOT EXISTS `readings`
    (`ReadingID` INT(11) NOT NULL AUTO_INCREMENT,
    `Datetime` DATETIME NOT NULL,
    `NOx` FLOAT DEFAULT NULL,
    `NO2` FLOAT DEFAULT NULL,
    `NO` FLOAT DEFAULT NULL,
    `PM10` FLOAT DEFAULT NULL,
    `NVPM10` FLOAT DEFAULT NULL,
    `VPM10` FLOAT DEFAULT NULL,
    `NVPM2.5` FLOAT DEFAULT NULL,
    `PM2.5` FLOAT DEFAULT NULL,
    `VPM2.5` FLOAT DEFAULT NULL,
    `CO` FLOAT DEFAULT NULL,
    `O3` FLOAT DEFAULT NULL,
    `SO2` FLOAT DEFAULT NULL,
    `Temperature` REAL DEFAULT NULL,
    `RH` INT DEFAULT NULL,
    `AirPressure` INT DEFAULT NULL,
    `DateStart` DATETIME DEFAULT NULL,
    `DateEnd` DATETIME DEFAULT NULL,
    `Current` TEXT DEFAULT NULL,
    `InstrumentType` VARCHAR(32) DEFAULT NULL,
    `Stationid_fk` INT,
    PRIMARY KEY (`ReadingID`));"""

    schema_sql = """CREATE TABLE IF NOT EXISTS `schema`
    (`SchemaID` int(3) NOT NULL AUTO_INCREMENT,
    `Measure` VARCHAR(32) DEFAULT NULL UNIQUE,
    `Description` text NOT NULL,
    `Unit` text NOT NULL,
    PRIMARY KEY (`SchemaID`));
    """
    # Executing the creation of the tables
    cur.execute(stations_sql)
    cur.execute(readings_sql)
    cur.execute(schema_sql)

    # Adding the relationships between the tables
    cur.execute("ALTER TABLE readings ADD FOREIGN KEY (`Stationid_fk`) REFERENCES stations(`Stationid`);")


    # Reading in the csv file
    with open('clean.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Attaching the rows in the csv file to a list
        for row in reader:
            records.append(row)

        # Removing the header from the list
        records.pop(0)

        # Printing the length of the records to confirm if it is correct.
        # print(len(records))

    # Getting the first 100 rows of the record
    for row in records:
        # set the autocommit flag to false
        conn.autocommit = False

        # sql query to insert the station records
        stations_sql = """INSERT IGNORE INTO stations (`Stationid`, `Location`, `geo_point_2d`) VALUES (%s, %s, %s)"""
        station_values = (row[4], row[17], row[18])
        cur.execute(stations_sql, station_values)

        # get stationid using SQL since using INSERT IGNORE above
        cur.execute("SELECT Stationid from stations WHERE location = ?", (row[17],))

        # Querying the result for the station_id
        station_id = cur.fetchone()[0]

        # sql code to insert the readings records
        readings_sql = """INSERT IGNORE INTO readings VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s)"""
        reading_values = ("", row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                          row[12], row[13], row[14], row[15], row[16], row[19], row[20], row[21], row[22], station_id)
        cur.execute(readings_sql, reading_values)

    #conn.commit()

    # SQL code to insert into the schema table
    schema_query = 'INSERT IGNORE INTO `schema` (Measure, Description, Unit) VALUES (%s, %s, %s)'
    schema_values = [('Date Time', 'Date and time of measurement', 'datetime'),
                     ('NOx', 'Concentration of oxides of nitrogen', 'μg/m3'),
                     ('NO2', 'Concentration of nitrogen dioxide', 'μg/m3'),
                     ('NO', 'Concentration of nitric oxide', 'μg/m3'),
                     ('SiteID', 'Site ID for the station', 'integer'),
                     ('PM10', 'Concentration of particulate matter <10 micron diameter', 'μg/m3'),
                     ('NVPM10', 'Concentration of non - volatile particulate matter <10 micron diameter', 'μg/m3'),
                     ('VPM10', 'Concentration of volatile particulate matter <10 micron diameter', 'μg/m3'),
                     ('NVPM2.5', 'Concentration of non volatile particulate matter <2.5 micron diameter', 'μg/m3'),
                     ('PM2.5', 'Concentration of particulate matter <2.5 micron diameter', 'μg/m3'),
                     ('VPM2.5', 'Concentration of volatile particulate matter <2.5 micron diameter', 'μg/m3'),
                     ('CO', 'Concentration of carbon monoxide', 'mg/m3'),
                     ('O3', 'Concentration of ozone', 'μg/m3'),
                     ('SO2', 'Concentration of sulphur dioxide', 'μg/m3'),
                     ('Temperature', 'Air temperature', '°C'),
                     ('RH', 'Relative Humidity', '%'),
                     ('Air Pressure', 'Air Pressure', 'mbar'),
                     ('Location', 'Text description of location', 'text'),
                     ('geo_point_2d', 'Latitude and longitude', 'geo point'),
                     ('DateStart', 'The date monitoring started', 'datetime'),
                     ('DateEnd', 'The date monitoring ended', 'datetime'),
                     ('Current', 'Is the monitor currently operating', 'text'),
                     ('Instrument Type', 'Classification of the instrument', 'text')
                     ]
    cur.executemany(schema_query, schema_values)
    conn.commit()
    conn.close()

# catch and report exception errors
# exit with 1 (non-error scripts automatically exit with 0)
except BaseException as err:
    print(f"An error occurred: {err}")
    sys.exit(1)
