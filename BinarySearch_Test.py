import unittest #for unit testing

#class for unit testing
class TestSearch(unittest.TestCase):	
	def test1(self):
		print "Number to be searched for test1 = 5"
		self.assertEqual(getInput("input", 5), True)
	def test2(self):
		print "Number to be searched for test1 = 5"
		self.assertEqual(getInput("random", 5), False)


#class for binary search algorithm
class BinarySearch:
	arr = []
	#constructor
	def __init__(self, a):
		self.arr = a 

	#algorithm for quick sort
	def Partition(self, p, q):
		pivot = self.arr[p]
		i = p #ith index starts at pivot
		for j in range(p+1, q+1):
			if self.arr[j] < pivot:
				i += 1
				#swap ith and jth elements				
				self.arr[i], self.arr[j] = self.arr[j], self.arr[i]			 
		#swap position of pivot
		self.arr[i], self.arr[p] = self.arr[p], self.arr[i]	 
		return i

	def QuickSort(self, p, q):
		if p < q:
			r = self.Partition(p, q)
			self.QuickSort(p, r-1)
			self.QuickSort(r+1, q)
		return self.arr

	#algorithm for binary search
	def Search(self, key, low, high):
		if low<high:
			mid = low+(high-low)/2
			if key == self.arr[mid]:
				return mid
			elif key < self.arr[mid]:
				return self.Search(key, low, mid)
			else:
				return self.Search(key, mid+1, high)
		else:
			return -1

#input from file and sort, search here
def getInput(filename, key):
	a = []
	#get input from file into array
	try:
		with open(filename, 'r') as  infile:
			for line in infile:
				a.append(int(line))
		infile.close()
		#sort array
		s = BinarySearch(a)
		s.QuickSort(0, len(a)-1)
		# sort = QuickSort(a)
		# sort.Quick(0, len(a)-1)
		#search array for key
		# search = BinarySearch(a)		
		index = s.Search(key, 0, len(a)-1)
		if (index+1):
			print "Number found at ", index
			return True
		else:
			print "Number not found!"
			return False
	except Exception as e:
		print "Exception: "+str(e)
	return False

#call search here
def main():
	filename = raw_input("Enter file name for input array: ")
	searchkey = raw_input("Enter number to be searched: ")
	getInput(filename, searchkey)

#test main here
main()
print "**********"
unittest.main()