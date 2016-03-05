# Find the kth node in the linked list from the end.
# place 2 pointers.1 should be k behind the other.Than way when the 2nd one reaches the end.You know 1st is at k 

class Node:

	def __init__(self,data,nextnode=None):
		self.data=data
		self.nextnode=nextnode

	def get_data(self):
		return self.data


class LinkedList:

	def __init__(self,head=None):
		self.head=head

	def insert(self,num):
		node=Node(num)
		if self.head is None:
			self.head=node
		else:
			current=self.head
			while(current.nextnode!=None):
				current=current.nextnode
			current.nextnode=node

	def traverse(self,k):
		i=1
		current=self.head
		while(True):
			current=current.nextnode
			i=i+1
			if i>k:
				return current


def get_kth_from_tail(llist,k):

	p1=llist.traverse(k)
	p2=llist.traverse(1)

	while(p1.nextnode):
		p1=p1.nextnode
		p2=p2.nextnode

	print(p2.data)

def main():
	ls=[1,2,3,4,5,6,7,8,9,11,12]
	llist=LinkedList()
	for value in ls:
		llist.insert(value)

	get_kth_from_tail(llist,5)


if __name__ == '__main__':
	main()



