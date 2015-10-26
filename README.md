SemanticWebAnalysis

Python package for the storage of semantic web data

Uses RDF triples to store linked data (stores string and url for  predicate and object )
Creates sqlite databasse instance for an inputted topic
takes topic name as input to intitialize creator
data must be pulled and takes a link to semantic data as input (call staticmathed exampleURLs() for example URLs)
Data must be processed and stored using processData() 
This method takes the results form getData() 
Then store the data in the sqlite table using storeData() with input processed data


Subject is stored as the database location
locator is used to create binary search tree based on folder location and name of database files (generated key (name) and value (DB location))

