INTRODUCTION:

This is a simple server for assignment 3.
You may change the source code as you see fit, so long that running it remains the same.

In order to run the server you must have python 2.x installed (Information Systems and Computer Science labs have it installed).


In order to run the server on Computer Science lab computers do the following:
1) Download the server from moodle.
2) Open konsole and traverse to the directory containing server.py
3) Run it using the command: python server.py

In order to get to the website - open your browser (chrome, preferably) and type in the address box the following:
localhost:8080

You will be automatically directed to the index.html appropriate to your device (desktop or mobile)
------------------------------
WEBSITE STRUCTURE:

The desktop version of your website must be in the desktop directory, while the mobile version in the mobile directory.
Each one of those directories must contain an index.html so that it may run properly.

*The example website does not contain an index.html for the mobile version.

The shared directory is for files shared between both versions. There are examples for using it - go over them.
For your convenience, AngularJS is already installed under shared/js/angular.min.js
------------------------------
DATA:

-------------
You can change the data-set as you see fit in the data.py file.

The data is represented by a dictionary in python (https://docs.python.org/2/tutorial/datastructures.html#dictionaries). The dictionary is practically the same as a JSON (which we have went over during our JS lessons), and so you are expected to be able to change it.

The data is represented by a collection name (e.g. "dogs") for the key. 
The value of a collection is a list of dictionaries (you can think of them as JSONs), representing elements.
You can add collections and elements to a collection as you see fit.
-------------

API calls for data are through the /data/ and you must specify a data collection:
Example for getting the "dogs" collection from the server:
Make an HTTP GET request to "/data/?_collection=dogs"

You can ask for all of the dogs from index 1 (index begins at 0!):
"/data/?_collection=dogs&_index=1"

If you specify and index that is too big you will get an empty list

You can ask for only 2 dogs:
"/data/?_collection=dogs&_length=2"
If the length is too big you will simply get the rest of the items.

Combining the two:
"/data/?_collection=dogs&_index=1&_length=2"

You can filter with specific values:
"/data/?_collection=dogs&name=Australian Shepherd"

Or category:
"/data/?_collection=dogs&size=small"

Just remember - by specifying a small list, the index might be too big!

Take note: these API calls are made to the server listening on localhost:8080, as in, you prepend the localhost:8080 prefix to each one of them.
------------------------------
MOBILE:

By using the Google Chrome device simulator you can see the mobile version of your website.
The server automatically picks the files from the mobile directory when the User Agent indicates a mobile device.