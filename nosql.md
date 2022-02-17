# **MongoDB Implementation Report**

I chose to use MongoDB in implementing my NoSQL database. my reasons for choosing MongoDB include: 

<ol>
<li> The extensive documentation that is available online. I got enough references to look up while researching and I also came across a lot of posts detailling the best approaches to implement mongodb databases. 
<li> MongoDB has a flexible schema, hence I am free to  choose how I wish to model my data <em>(1)</em>.
<li> MongoDB  supports a lot of programming languages. This made implementation very easy as I was able to use python to send my data into the mongodb database <em>(2)</em>.
<li> Of all the NoSQL databases, mongodb is the easiest to implement.
<li> It is arguably the most used NoSQL database, hence, as a budding data engineer I considered it a necessary tool for me to learn. 
</ol>

</br>

## **Implementation**

In my implementation I started by trying to understand how mongodb stores information in its database, I found out that databases are made up of collections of documents. Unlike SQL where data are saved in rows and columns, data in MongoDB are saved as keys and values within documents, the documents are then saved within a collection, while the collections are saved in a databse. Hence, documents hold keys and values, collections hold documents and databases hold collections.

In my research, I came across a number of approach to database implementation in mongodb and I considered which of them will best suite the task I had. First, I looked at embedding the readings data in the station document, however, in my research, I soon realised that this will make it difficult for me to query or access readings data as a standalone entity <em>(3)</em>.  

I also realised that embedding in this way will cause the document to exceed the 16mb BSON document size limit. As one site document will hold all the readings from that site<em>(4)</em>.

Another approach I thought of was to implement the database by creating two different collections for the stations and the readings data, while referencing the stations' object id in the respective readings document. However, querying the database this way was also going to be difficult. And I conclued that this was not the best approach.

I then opted for total denormalisation, which is one of the perks of NoSQL. This would mean that flat CSV file which contains the readings from the stations as well as the station details can be uploaded into the database, thereby saving all the different readings with all the corresponding site information as single documents in a collection called 'readings'. 

I went on to design a database schema that highlighted how my documents will look. I also specified the datatypes I intended to use for each of the attributes in the MongoDB document. 

The doubles datatype in Mongodb can be likened to the floats in SQL, the strings can be likened to VARCHAR, the date can be likened to datetime in SQL and the int are integers.

![Getting Started](mongodb_images/mongodb_schema.png)

The schema implementation would look like the image below

![Getting Started](mongodb_images/sample_schema_implementation.png)

In populating the database, I used the pymongo library in python to connect my vscode to my mongodb server. I established a connection with pymongo.MongoClient using the default host and port of MOngoDB and equated this to a variable called client.  

![Getting Started](mongodb_images/python_script.png)

I then used the client variable to create a database, and also created the collections that held the documents. I named the collection readings.  

I went on to import my CSV file using pandas and selected the columns I needed to convert to DateTime (as this is also possible in MongoDB) and converted them to DateTime format using pandas parse_dates. Then I selected all datasets with station ID 206 as the monitor station I chose to work with. 

I dropped all duplicate values (this I did just as a validator that there aren't any duplicate values passed into my database), and then converted all the datasets to dictionaries while customising the key-value pair by setting orient to RECORDS (column -> value). 

I used the insert_many function to send all the data values to the MongoDB database. 

Here is a sample from the database implementation. 

![Getting Started](mongodb_images/mongodb_documents.PNG)


Here are the sample queries that were performed on the database: 

Loading 1 document (row of data) from the collection:
![Getting Started](mongodb_images/DB_Queries.PNG)

Loading 1 reading where the Nitrogen Oxide level greater than 800
![Getting Started](mongodb_images/DB_Queries2.PNG)

Loading a reading taken on the 23rd of August 2013. 
![Getting Started](mongodb_images/DB_Queries3.PNG)



## References: 
<ol>
<li> https://docs.mongodb.com/manual/data-modeling/ </li>
<li> https://www.geeksforgeeks.org/mongodb-an-introduction/#:~:text=Language%20Support%20by%20MongoDB%3A,Scala%2C%20Go%2C%20and%20Erlang </li>
<li> https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1 </li>
<li> https://docs.mongodb.com/manual/reference/limits/ </li>

</ol>



