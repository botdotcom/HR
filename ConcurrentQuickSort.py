'''Concurrent Quick Sort algorithm.
Unit testing is also performed.
'''
import xml.etree.ElementTree as x 
import threading
import unittest

#class for unit testing
class TestClass(unittest.TestCase):
	def test1(self):
		print "Test1"
		self.assertEqual(callfunction("input.xml"),True)
	def test2(self):
		print "Test2"
		self.assertEqual(callfunction("random"),False)


#class for quick sort
class Sort:	
	arr = []
	def __init__(self, a):		
		self.arr = a
		
	def Partition(self, p, q):
		pivot = self.arr[p]
		i = p #ith insex at pivot at start
		for j in range(p+1, q+1):
			if self.arr[j] < pivot:
				i += 1
				self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
		self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
		return i

	def Quick(self, p, q):
		if p < q:
			r = self.Partition(p, q)
			print threading.current_thread().getName(), " thread found mid = ", r
			t1 = threading.Thread(target=self.Quick, args=(p, r-1))
			t1.start()
			t2 = threading.Thread(target=self.Quick, args=(r+1, q))			
			t2.start()
			t1.join()
			#print t1.getName()
			t2.join()
			#print t2.getName()
		return self.arr

def callfunction(filename):
	try:
		xmltree = x.parse(filename)
		root = xmltree.getroot()
		a = []
		for child in root:
			a.append(int(child.text))
		print "Unsorted array:\n", a
		#call sort function
		s = Sort(a)
		quick = s.Quick(0, len(a)-1)
		print "Sorted array:\n", a
		return True
	except Exception as e:
		print "Exception: "+str(e)
		return False

def main():
	callfunction("input.xml")

#test
unittest.main()