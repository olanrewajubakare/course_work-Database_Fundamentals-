USE `pollution-db2`;

SELECT readings.Datetime, readings.NOx, stations.Location FROM `readings`
INNER JOIN `stations` ON readings.Stationid_fk = stations.Stationid
AND readings.NOx = (SELECT MAX(NOx) FROM readings
WHERE Datetime >= '2019-01-01 00:00:00' AND Datetime < '2020-01-01 00:00:00');