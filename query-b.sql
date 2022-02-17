USE `pollution-db2`;

SELECT s.*, AVG(`PM2.5`), AVG(`VPM2.5`) FROM Stations s
INNER JOIN readings r ON r.Stationid_fk = s.Stationid
WHERE Datetime >= '2019-01-01 00:00:00' AND Datetime < '2020-01-01 00:00:00'
# makes it inclusive for a datetime type
	AND Datetime LIKE '%08:00%'
    # gets the hour of the day from the datetime 
GROUP BY s.Stationid;