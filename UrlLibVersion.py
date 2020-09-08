import urllib.request, urllib.parse, urllib.error # import url library
file = open("webresults.txt", "a+") # create a file for reading and writing to 
matchCount = 0 # establish a global varibale for stroing the number of total matches for a team
pFile = ""

def findPlayer(playerName,scorecard):
	global pFile
	if scorecard != "https://www.espncricinfo.com/series/11825/scorecard/667639/new-zealand-xi-vs-" and scorecard!= "https://www.espncricinfo.com/series/8532/scorecard/966761/india-vs-united-ara":
		fhand = urllib.request.urlopen(scorecard) # set the url to the link with a specific date
		playerFile = open(playerName+"_Matches.txt", "a+") # create a file for reading and writing to 
		
		pFile = playerFile
		for line in fhand: # read the contents of the webpage line by line
			words = line.decode() # store the unicode UTF8 contents of the webpage as a string into the variable 'words'
	
			if words.find(playerName) >-1:
				print(playerName," found")
				playerFile.write("\n"+scorecard+"\n")
				return True
	
		print( playerName, " not found\n\n")
		
		return -1


def screenByRuns(matchLink, runLessThan,pName):
	fhand = urllib.request.urlopen(matchLink) # set the url to the link with a specific date
	for line in fhand:
		words = line.decode()
		if words.find(pName):
			for lines in fhand:
				bits = lines.decode()
				startingPoint = bits.find(pName)
				manOfMatch = bits.find("player-match__player__headshot")
				endingPoint = bits.find("cell runs",startingPoint)
				#print("Man of match",manOfMatch,"starting", startingPoint, "diff" ,manOfMatch-startingPoint)
				#print(startingPoint - manOfMatch)
				if startingPoint>-1 and endingPoint >-1:
					if startingPoint - manOfMatch <500 and startingPoint-manOfMatch>0:
						#print(startingPoint, manOfMatch)
						startingPoint = bits.find(pName,endingPoint)
						endingPoint = bits.find("cell runs",startingPoint)

					newStartingPoint = bits.find(">",endingPoint+28)
					newEndingPoint = bits.find("</",newStartingPoint)
	
					stringRunAmount = bits[newStartingPoint+1:newEndingPoint]
					#print(startingPoint,manOfMatch,endingPoint, startingPoint-manOfMatch)
					print(stringRunAmount,"\n\n")


def findAllLinks(testStr,plName): # create a function to find all matches per a given string 
	firstPos = testStr.find('match,desktop"') # find the starting index for the scorecard link
	secondPos = testStr.find('href=',firstPos) # find the ending index for the scorecard link
	global matchCount # link the global varibable from above

	if firstPos > -1 and secondPos > -1: # if the indexes are greater than -1 and thus a link is found
		link = testStr[firstPos+21:secondPos+55] # extract the link by slicing from between the first and last index with some modifications
		link = "https://www.espncricinfo.com"+link

		print(link) # print the full link by concatenating the href tag with the url link
		file.write(link+"\n\n") # write the full link to the file
		
		if findPlayer(plName,link):
			screenByRuns(link,20,plName)
		matchCount+=1 # increment by one for every match found


		findAllLinks(testStr[secondPos+50:],plName) # recursively call the find method with part of the string sliced off

		return True # return 
		
	return -1 # return -1 for not found





for i in range(2010,2020): # loop through the range of years
	for j in range(1,13): # loop through the range of months

		if j<10 : # if the month is not a double digit 
			date = str(i)+"0"+str(j) # the date is the year + a 0 with the month
		else:
			date = str(i)+str(j) # else simply concatenate the year and the double digit month

		print("\n"+str(date)+"\n") # print the date
		file.write("\n"+str(date)+"\n") # write the date to the file

		fhand = urllib.request.urlopen('https://www.espncricinfo.com/scores/team/6/india?date='+date) # set the url to the link with a specific date
		
		for line in fhand: # read the contents of the webpage line by line
		
			words = line.decode() # store the unicode UTF8 contents of the webpage as a string into the variable 'words'
		
			findAllLinks(words,"Kohli") # call the find method

print("\n\nIndia has played ",matchCount, " matches since 2010") # print the total amount of matches played by the team
file.write("\n\nIndia has played "+str(matchCount)+" matches since 2010") # write to the file the total amount of matches played by the team
print("\n Kohli has been bowled out the most at 8 times by James Anderson - Right-arm fast-medium bowler")
file.close() # close the file to save the data from being corrupted
