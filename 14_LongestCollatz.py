import unittest
import time

class Collatz:

	def __init__(self,start):
		self.start=start
		self.next_in_seq=start
		self.sequence_count=1

	def __iter__(self):
		return self

	def next(self):
		if self.next_in_seq==1:
			raise StopIteration

		elif self.next_in_seq%2==0:
			self.next_in_seq=int(self.next_in_seq/2)

		else:
			self.next_in_seq=int(3*self.next_in_seq)+1

		self.sequence_count+=1
		return self.next_in_seq

	def get_series_count(self):

		try:
			generator=Collatz(self.start)
			while(StopIteration):  
				generator.next()
		except StopIteration:
			return generator.sequence_count


def main():

	collatz_dict=dict()
	for num in range(1,1000000):
		num_collatz=Collatz(num)
		collatz_dict[num]=num_collatz.get_series_count()
	print(max(collatz_dict,key=collatz_dict.get))



if __name__ == '__main__':
	starttime=time.time()
	main()
	print(time.time()-starttime)




