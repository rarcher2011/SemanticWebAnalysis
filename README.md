SemanticWebAnalysis

Python package for the storage of semantic web data

Uses RDF triples to store linked data (stores string and url for  predicate and object ). Creates sqlite databasse instance for an input topic.
Takes topic name as input to intitialize creator class (SemWeb.creator.creator()).
Data must be pulled and takes a link to semantic data as input (call staticmathed exampleURLs() for example URLs).
getData() takes the argument of a semanti web link.
Data must be processed using processData(). 
This method takes the results from getData() as input.
Then store the data in the sqlite table using storeData() with the input as the return value from processData().


Subject is stored as the database location
locator is used to create binary search tree based on folder location and name of database files (generated key (name) and value (DB location))

