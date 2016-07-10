import socket

#Setting the socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect( ('www.pythonlearn.com', 80) )

#Making the HTTP request that will get us the desired document
mysocket.send("GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0 \n\n")

while True:
	#Obtaining the web data
	webdata = mysocket.recv(512)

	#When there's no more data left, we'll stop the loop
	if len(webdata) < 1:
		break

	#Printing the obtained data
	print webdata

mysocket.close()