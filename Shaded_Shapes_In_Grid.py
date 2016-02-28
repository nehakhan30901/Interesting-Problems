#We have a grid with certain shaded cells.All connected cells are considered 1 shape.Find how many shapes 
#does the grid have 

import unittest

class Node:
	#Class variable to track number of nodes
	id=0

	#constructor
	def __init__(self,cordinates,data):
		Node.id+=1
		self.obj_id=Node.id
		self.cordinates=cordinates
		self.data=data
		self.neighbour_nodes=[]
		self.visited=False  #this flag will be used while traversing the node for shapes

	#setter
	def set_data(self,value):
		self.data=value

	def get_neighbour_cordinates(self):
		x=self.cordinates[0]
		y=self.cordinates[1]
		#neighbour_cordinates=[(x-1,y),(x+1,y),(x,y-1),(x,y+1),(x-1,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1)]
		neighbour_cordinates=[(x+1,y),(x,y+1),(x+1,y+1),(x+1,y-1)]#Try to move forward only considering 
																  #last shapes are already traversed
		return neighbour_cordinates

class Matrix:

	def __init__(self,row,column):
		Node.id=0
		self.row=row
		self.column=column
		self.matrix=[[None for j in range(0,column)] for i in range(0,row)] 
		for i in range(0,row):
			for j in range(0,column):
				node=Node((i,j),False)
				self.matrix[i][j]=node

	def show_matrix(self):
		matrix_str=''
		for i in range(len(self.matrix)):
			matrix_str=matrix_str+'\n'
			for j in range(len(self.matrix[i])):
				matrix_str=matrix_str+str(self.matrix[i][j].data)+'\t'
		print(matrix_str)	

	def get_neighbours(self,node,debug=0):
		neighbour_cordinates=node.get_neighbour_cordinates()
		if debug==1:
			print(neighbour_cordinates)
		neighbour_nodes=[]
		for each in neighbour_cordinates:	
			x=each[0]
			y=each[1]
			if x>=0 and x<self.row and y>=0 and y<self.column:
				if debug==1:
					print(x,y)
				neighbour_nodes.append(self.matrix[x][y])
			else:
				continue
		node.neighbour_nodes=neighbour_nodes

	def build_graph(self):
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[i])):
				self.get_neighbours(self.matrix[i][j])

	#Heart of the program.This function will count 1 for each shaded cell and traverse to all its neighbours
	#recursively to mark them visited for shape 1.The next iteration picks up a shaded cell which has not being
	#marked visited.Meaning it was not connected to any previous traversals,hence a new shape
	def find_shapes(self):
		shaded_cells=list()
		shape_count=0
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[i])):
				if self.matrix[i][j].data==True:
					shaded_cells.append(self.matrix[i][j])
		for eachcell in shaded_cells:
			if eachcell.visited==False:
				shape_count=shape_count+1
				self.traverse_shape(eachcell)
		return shape_count


	def traverse_shape(self,shaded_node):
		neighbours=shaded_node.neighbour_nodes
		for each in neighbours:
			if each.data==True:
				each.visited=True
				self.traverse_shape(each)
			else:
				continue

#Test Cases
class test(unittest.TestCase):
	@unittest.skip("not required")
	def test_initialize_matrix(self):
		m=Matrix(3,5)
		m.show_matrix()
		
	@unittest.skip("not required")
	def test__get_neighbour_cordinates(self):
		m=Matrix(3,5)
		node=m.matrix[0][0]
		print(node.get_neighbour_cordinates())

	@unittest.skip("not required")
	def test__get_neighbour(self):
		m=Matrix(3,5)
		node=m.matrix[0][0]
		self.assertEqual(len(m.get_neighbours(node)),3)
		node=m.matrix[1][1]
		self.assertEqual(len(m.get_neighbours(node)),8)

	@unittest.skip("not required")
	def test_display_tree(self):
		m=Matrix(3,5)
		m.build_graph()
		m.display_tree()

	def test_find_shapes(self):
		m=Matrix(3,5)
		m.build_graph()
		m.matrix[0][0].set_data(True)
		m.matrix[0][1].set_data(True)
		m.matrix[1][2].set_data(True)
		m.matrix[2][1].set_data(True)
		m.matrix[0][4].set_data(True)
		m.matrix[2][4].set_data(True)
		m.matrix[1][0].set_data(True)
		self.assertEqual(m.find_shapes(),3)


if __name__ == '__main__':
	unittest.main()







