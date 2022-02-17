# **Reflective Report**

The assignment can be looked at as a practical exercise that covered all the topics that we looked at in the course. It was an opportunity for me to learn a lot about the concept of data management, as this was somewhere I had very little experience in. 

Before the commencement of my program in school, I took out time to study python as well as the basics of data science. This came in handy, as I was able to handle most of the tasks in the assignment with ease. 

The tasks aimed to teach us how to model, cleanse, normalize, shard, map, query and analyze substantial real-world big data. 

The first task which involved cleaning the data set was split into two parts. Handling the first part was quite straightforward, as all that was required of us was to drop records before the first of January 2010. I did this using the pandas library. I opened the file with the pandas.read_csv function, and then set the delimiter, as it occurred in the file.

In ensuring that I dealt with the low memory error caused by the mixed type inference, I had to set the low_memory parameter to false. Using the datetime function in pandas, I then initiated my dataframe to only contain data from the 1st of January 2010. 

Although this approach was very straightforward and short, I found out that it was quite slow and hence, and it will take a lot longer when handling larger files. I found the approach shared by lecturer during his code reveal very fascinating, however, I wanted my scripts to be different from the rest of the class. Hence, I decided to stick with using pandas. 

For the second task, I read the cropped file using pandas and then created a dictionary that held the right siteID as the key as well as the corresponding station name as the values. I made a copy of the dataframe, then looped through the dictionary and made the copied dataframe to only hold the mismatched values (i.e. df2 was made to hold only wrong/mismatched values). By comparing df2 to the original dataframe, I dropped all the values in the original dataframe that had their indexes occurring in df2. Effectively making df hold the correct values.  

I found this approach to be a lot cleaner than all the other solutions I came up with. And I was sure that it would be very different from that of the rest of the class. 

The second task of the assignment involved creating an ER model. I used workbench for this one, and then used the forward engineering feature in workbench to create the database. This was super easy for me as I know how to use multiple design softwares. 

The third task involved writing a python script to populate MySQL database. For this task, I used MariaDB as well as the CSV library in python. I decided against using pandas for this task as the CSV library provided a faster way to read csv files, this meant that populating the database will be faster. I established a connection between Python and MariaDB using the appropriate user, password, host and port number. I then created the database as well as the tables. I looped through the rows in the CSV file and then appended each of the rows to an empty list. I used the 'insert ignore' query to ensure that I did not insert any duplicate values into the database. And to insert the ‘schema’ table, I entered the values into my script and used the 'insert many' function in python to insert the values. 

The fourth task involved writing SQL queries. This was a nice way to practice writing SQL queries. I used a better approach in writing my first query for the task by selecting the necessary values from the two tables and then joining them on the station id, then using the AND function to select the maximum NOx from the readings table where the date is 2019. Another approach I could have used instead of using this was to arrange my rows of values from 2019 in descending order by the NOx values, and then set the limit to 1, thereby, picking the highest value NOx in the table. 

For the fifth task, I used MongoDB to implement my NoSQL database, and I wrote a python script to populate my database. I populated the database with the denormalised data which is the cleaned CSV file. I also specified the right data types for each attribute in the documents. I then went on to write some queries to demonstrate the efficiency of the database. 

The assignment was like a project that gave me the opportunity to put to use all that I had been taught while also giving me the opportunity to learn a lot about databases and their adjoining concepts. 


