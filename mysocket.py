import socket # import socket library to begin interreaction with the web

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # establish a socket without actually connecting to anything, kind of like creating an IO fstream
mysock.connect(('data.pr4e.org',80)) # connect to the host and socket number

urlbit = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'

cmd = 'GET http://www.espncricinfo.com/ HTTP/1.0\r\n\r\n'.encode() # create a get request command 
mysock.send(cmd) # send the get get request

file = open("webresults.txt", "a+") # create a file for reading and writing to 

charCount = 0
while True: 
	data = mysock.recv(1024) # accept data up to 1024 characters in one buffer
	charCount+=len(data)
	if(len(data)<1): # if the data length is less than 1 eof and break
		break

	file.write(data.decode()) # write to the file the data gotten from the web
	file.write("\n") # insert a new line character to seperate data
	print(data.decode()) # print the decoded data to console

print("\n",charCount)
file.write("\nCharacter Count Total: ")
file.write(str(charCount))

mysock.close() # close socket and bream connection
file.close() # close the file

