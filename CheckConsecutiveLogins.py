'''
Given a text file containing this information (Date the customer logged-in, Tab,
Customer ID)
Example:
04/11/2017 \t 0003
04/12/2017 \t 0003
04/13/2017 \t 0004
04/13/2017 \t 0003
04/13/2017 \t 0003
04/15/2017 \t 0004
How to get the list of those customers that log in on four consecutive days?
'''

import re
from collections import defaultdict
import time
import datetime

def main():	
	log = defaultdict(list)	
	result = [] #array of repeats
	with open('customer_log.txt', 'r') as infile:
		lines = infile.readlines()
		#create list
		for line in lines:
			line = re.split("\t", line.strip())			
			log[line[1]].append(datetime.datetime.strptime(line[0], "%m/%d/%Y"))
			log[line[1]].sort()						
		#compare dates		
		for key, val in log.items():			
			x = len(val) #count of total login dates for a customer
			count = 0
			#comparison loop
			for i in range(0,x-1):
				if (val[i+1] - val[i]).days == 1:					
					count += 1				
			#for 4 consecutive logins
			if count == 3:
				result.append(key)
		#display all such customers result
		print result
	
main()