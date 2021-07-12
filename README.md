This repo contains the back-end of the yt-scraper with the APIs in node.js using express and MongoDb and python script to scrape the data.
The python script scrapes and stores the data into MongoDb cloud and APIs are designed to access that data and perform.
The python script does not scrape 'video thumbnail' as of now because of a issue that I faced.

For python script- INSTALLATION OF REQUIRED MODULES
pip install -U selenium
https://www.geeksforgeeks.org/how-to-install-selenium-in-python/
pip install pymongo[srv]


MongoDB update database
Here we have deleted all the documents and inserted the previous documents
If we try to update the documents, then that would be just an overhead for processing, because we actually
only want the recent videos to be populated in the database which we actually have,
so its better to insert them instead of updating them.


To run:
  run -> npm start and the server will be up and running
