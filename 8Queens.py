'''Solved 8 Queens' matrix problem using backtracking.
Unit testing also included.
Input is from .json file of the form:

{"start": 1}
'''
import unittest
import json

class TestClass(unittest.TestCase):
	def test1(self):
		print "Test 1:"
		self.assertEqual(callfunction("input2.json"),True)
	# def test2(self):
	# 	print "Test 2:"
	# 	self.assertEqual(callfunction("input3.json"),False)

class EightQueens():
	def CheckPlace(self, board, row, col):
		for i in range(row):
			if board[i][col] == 1:
				return True
		#check first half of board
		i = row - 1
		j = col - 1
		while i>=0 and j>=0:
			if board[i][j] == 1:
				return True
			i -= 1
			j -= 1
		#check second half of board
		i = row - 1
		j = col + 1
		while i>=0 and j<8:
			if board[i][j] == 1:
				return True
			i -= 1
			j += 1
		return False

	def Queen(self, board, row):
		i = 0
		while i<8:
			if not self.CheckPlace(board, row, i):
				board[row][i] = 1
				if row == 7:
					return True
				else:
					#backtracking step
					if self.Queen(board, row+1):
						return True
					else:
						board[row][i] = 0
			i += 1
		if i == 8:
			return False

	def PrintBoard(self, board):
		for i in range(8):
			for j in range(8):
				print str(board[i][j])+" ",
			print "\n"

def callfunction(filename):
	board = [[0 for x in range(8)] for x in range(8)] #create a 8x8 board
	data = []
	q = EightQueens()
	with open(filename, 'r') as infile:
		data = json.load(infile)
	if data["start"]<0 or data["start"]>7:
		print "Invalid input!"
		return False
	board[0][data["start"]] = 1
	if q.Queen(board, 1):
		print "Problem solved!\nBoard configuration:"
		q.PrintBoard(board)
		return True
	else:
		print "Problem not solved!"
		return False

#call main and test
callfunction("input1.json")
unittest.main()