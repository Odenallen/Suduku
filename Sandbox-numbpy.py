import numpy as np
import random as rn

class Suduku:
	def __init__(self,number = None):
		
		self.number = number



def initiateSuduku():
	matrix = np.empty((9,9), dtype = object)
	sudukulist = [[0,0,0,0,8,4,0,0,3],[1,3,0,0,5,0,0,9,4],[9,0,5,0,1,3,0,7,0],[4,0,0,0,9,6,0,0,0],[0,0,3,7,0,0,0,0,1],[7,5,0,0,3,0,4,6,9],[5,0,4,0,7,8,0,2,0],[3,6,0,0,2,9,0,5,0],[0,2,0,0,0,0,3,0,7]]
	for y in range(9):

		for x in range(9):
			matrix[x][y]=sudukulist[x][y]
			

	print(matrix)
	return matrix

def findUsedNumber(yCoordinate,xCoordinate):
	numberList = [1,2,3,4,5,6,7,8,9]
	incorrectNumber = []
	
	
	#check the row

	for i in range(9):
		if matrix[yCoordinate,i] in numberList:
			incorrectNumber.append(matrix[yCoordinate,i])

	
	#Check the column
	for a in range(9):
		if matrix[a,xCoordinate] in numberList and matrix[a,xCoordinate] not in incorrectNumber:
			incorrectNumber.append(matrix[a,xCoordinate])
	

	#Check and see what square the number is in and then add the numbers in the square to the incorrect number list
	
	if yCoordinate <= 2 and xCoordinate <=2:
		#square 1
		incorrectNumber=checkSquare(0,2,0,2,incorrectNumber)
		
	elif yCoordinate <= 2 and 2< xCoordinate <=5 :
		#square 2
		incorrectNumber=checkSquare(0,2,3,5,incorrectNumber)
		

	elif yCoordinate <= 2 and 5< xCoordinate:
		#square 3
		incorrectNumber=checkSquare(0,2,6,8,incorrectNumber)
			

	elif  2<yCoordinate <=5 and xCoordinate <=2 :
		#square 4
		incorrectNumber=checkSquare(3,5,0,2,incorrectNumber)
		

	elif  5<yCoordinate  and xCoordinate <=2 :
		#square 7
		incorrectNumber=checkSquare(6,8,0,2,incorrectNumber)
		
	elif  2<yCoordinate<=5 and 2<xCoordinate<=5 :
		#square 5
		incorrectNumber=checkSquare(3,5,3,5,incorrectNumber)
		
	elif  2<yCoordinate<=5 and 5<xCoordinate :
		#square 6
		incorrectNumber=checkSquare(3,5,6,8,incorrectNumber)
		

	elif  5<yCoordinate and 5<xCoordinate:
		#square 9
		incorrectNumber=checkSquare(6,8,6,8,incorrectNumber)
		
	else:
		#square 8
		incorrectNumber=checkSquare(6,8,3,5,incorrectNumber)
	
	return incorrectNumber

def checkSquare(yStart,yStop,xStart,xStop,incorrectNumber):
	valueX = xStart
	while True:
		if yStart <= yStop:
			if xStart != xStop:
				#first if statement
				if matrix[yStart][xStart] not in incorrectNumber and matrix[yStart][xStart] != 0:
					#print('we are adding %d %d to the list',yStart,xStart )
					incorrectNumber.append(matrix[yStart][xStart])
				
				xStart += 1
				
			elif xStart == xStop and yStart != yStop:
				if matrix[yStart][xStart] not in incorrectNumber and matrix[yStart][xStart] != 0:
					#print('we are adding %d %d to the list',yStart,xStart )
					incorrectNumber.append(matrix[yStart][xStart])
				xStart = valueX
				yStart += 1

			elif yStart==yStop and xStart==xStop:
				if matrix[yStart][xStart] not in incorrectNumber and matrix[yStart][xStart] != 0:
					incorrectNumber.append(matrix[yStart][xStart])
					
				break

		else:
				
			break

	return incorrectNumber
	


def recSolve():
	'''This function should work like a recursive function, it should itterate through
		the 





	'''




	pass

	


matrix = initiateSuduku()
incorrectMatrix = []

for y in range(9):
	for x in range(9):
		if matrix[y][x] == 0:
			
			incorrectNumber=findUsedNumber(y,x)
			incorrectMatrix.append(incorrectNumber)

			
			print(incorrectNumber)
			break
			#PUT BREAKING POINT HERE!!!!

	
print(incorrectMatrix)







