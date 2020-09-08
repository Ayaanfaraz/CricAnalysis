testString = 'jxfbanana1jxfbanana2jxfbanana3jxf'

# while True:

# 	firstPos = testString.find('ban')
# 	secondPos = testString.find('jxf',firstPos)

# 	fruit = testString[firstPos:secondPos]
# 	print(fruit)
# 	previousFruit = fruit

# 	if count >1 and fruit == previousFruit:
# 		break

	# could make a function and recursively throw in the string shortening it each time as a parameter
	

def findAllLinks(testStr):
	firstPos = testStr.find('ban')
	secondPos = testStr.find('jxf',firstPos)
	if firstPos > -1 and secondPos > -1:
		fruit = testStr[firstPos:secondPos]
		print(fruit)
	
		findAllLinks(testStr[secondPos:])

		return fruit
		
	return -1

print("----")
findAllLinks(testString)