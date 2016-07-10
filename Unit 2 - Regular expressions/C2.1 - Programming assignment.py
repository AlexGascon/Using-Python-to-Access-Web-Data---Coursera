import re

#Opening the file in which we'll need to find the numbers
sample_file = open('A.2.2 - regex text data.txt')

#Obtaining strings representing the numbers in that file
text = sample_file.read() #With read, we read the entire text and not line by line
number_regex = '[0-9]+'
numbers = re.findall(number_regex, text) #Match any combination of one or more digits

#Casting them to integers and getting the total sum
total = sum(int(num) for num in numbers)

print(total)

#Closing the file to avoid memory problems
sample_file.close()