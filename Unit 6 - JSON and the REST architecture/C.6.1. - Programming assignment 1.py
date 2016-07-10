""" EXTRACTING DATA FROM JSON
In this assignment you will write a Python program somewhat similar to 
http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read
the JSON data from that URL using urllib and then parse and extract the comment 
counts from the JSON data, compute the sum of the numbers in the file and enter 
the sum below:

We provide two files for this assignment. One is a sample file where we give you
the sum for your testing and the other is the actual data you need to process for
the assignment.
    
- Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
- Actual data: http://python-data.dr-chuck.net/comments_277465.json

You do not need to save these files to your folder since your program will read
the data directly from the URL. Note: Each student will have a distinct data url
for the assignment - so only use your own data url for analysis.


DATA FORMAT
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
The closest sample code that shows how to parse JSON and extract a list is 
json2.py. You might also want to look at geoxml.py to see how to prompt for a URL
and retrieve data from a URL. 
"""


import urllib
import json

sample_url = "http://python-data.dr-chuck.net/comments_42.json"
data_url = "http://python-data.dr-chuck.net/comments_277465.json"

#Reading the URL and parsing its data
urldata = urllib.urlopen(data_url).read()
data = json.loads(urldata)

#Finding each "count" field and adding its value to the total sum.
total = 0
for comment in data["comments"]:
	total += comment["count"]

print("TOTAL SUM: ", total)