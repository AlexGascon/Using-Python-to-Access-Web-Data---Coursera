"""
In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py
The program will use urllib to read the HTML from the data files below, extract
the href= vaues from the anchor tags, scan for a tag that is in a particular 
position from the top and follow that link, repeat the process a number of times,
and report the last name you find.


SAMPLE:
Find the link at position 3 (the first name is 1). Follow that link. Repeat this 
process 4 times. The answer is the last name that you retrieve. 
The result should be: Anayah

PROBLEM:
Find the link at position 18 (the first name is 1). Follow that link. Repeat this
process 7 times. The answer is the last name that you retrieve.
Hint: the name starts with S
"""

import urllib
from BeautifulSoup import *

#SAMPLE DATA
sample_url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
sample_repetitions = 4
sample_resultPosition = 3

#ACTUAL PROBLEM DATA
problem_url = "http://python-data.dr-chuck.net/known_by_Max.html"
problem_repetitions = 7
problem_resultPosition = 18


#Choosing the type of execution we're trying
type_of_execution = 'problem'
if type_of_execution == 'sample':
	(link, repetitions, resultPosition) = (sample_url, sample_repetitions, sample_resultPosition)

elif type_of_execution == 'problem':
	(link, repetitions, resultPosition) = (problem_url, problem_repetitions, problem_resultPosition)


#Amount of iterations needed
for times in range(repetitions):

	#Getting the information of the correspondent url
	html = urllib.urlopen(link).read()
	soup = BeautifulSoup(html)
	tags = soup('a')

	#We are indicated that the first name is 1, but in Python the array begins in 0,
	#so we have to take 1 unit from the index
	link = tags[resultPosition - 1].get('href')

#Getting the content of the tag in the specified position. It should correspond to
#the answer we're looking for
result_name = tags[resultPosition - 1].contents[0]
print(result_name)

