# LinAlg.py
# Nathan Greene
# Summer 2018

import math

class LinAlg:
	""" A collection of algebraic methods for vectors and matrices. Many of the
	methods contained were taken from Data Science from Scratch, by Joel Grus.
	"""

	@staticmethod
	def add_vectors(u, v):
		""" Adds two vectors component-wise returning a vector of the same
		length. """
		return [ui + vi for ui, vi in zip(u, v)]

	@staticmethod
	def subtract_vectors(u, v):
		""" Subtracts two vectors componet-wise returning a vector of the same
		length. """
		return LinAlg.add_vectors(u, LinAlg.scalar_multiply(-1, v))

	@staticmethod
	def scalar_multiply(a, v):
		""" Multiplies a scalar to each component of a vector returning a vector
		of the same length. """
		return [a * vi for vi in v]

	@staticmethod
	def multiply_vectors(u, v):
		return [ui * vi for ui, vi in zip(u, v)]

	@staticmethod
	def dot_product(u, v):
		""" Returns the dot product of two vectors. """
		return sum(LinAlg.multiply_vectors(u, v))

	@staticmethod
	def mean_vector(V):
		""" Returns a vector with each ith component being the mean value of the
		ith components of the set of vectors. """
		return LinAlg.scalar_multiply(1 / len(V), sum(V))

	@staticmethod
	def sum_squares(v):
		""" Returns the sum of the squared components of a vector. """
		return LinAlg.dot_product(v, v)

	@staticmethod
	def squared_difference(u, v):
		""" Returns a vector with components being the squared difference
		between two given vectors. """
		return LinAlg.sum_squares(LinAlg.subtract_vectors(u, v))

	@staticmethod
	def distance(u, v):
		""" Returns the Euclidean distance between two vectors. """
		return math.sqrt(LinAlg.squared_difference(u, v))

	@staticmethod
	def magnitude(v):
		""" Returns the magnitude of a vector. """
		return math.sqrt(LinAlg.dot_product(v, v))

	@staticmethod
	def shape(A):
		""" Returns the number of rows and columns in a matrix as a tuple. """
		return len(A), len(A[0]) if A else 0

	@staticmethod
	def is_square(A):
		""" Returns True if A is a square matrix and False if otherwise. """
		return True if LinAlg.shape(A)[0] == LinAlg.shape(A)[1] else False

	@staticmethod
	def row(A, i):
		""" Returns the ith row in matrix A. """
		return A[i]

	@staticmethod
	def column(A, i):
		""" Returns the ith column in matrix A. """
		return [row[i] for row in A]

	@staticmethod
	def matrix(m, n, fn):
		""" Returns an m x n matrix with entries defined by the function fn. """
		return [[fn(i, j) for j in range(n)] for i in range(m)]

	@staticmethod
	def is_diagonal(i, j):
		""" Returns 1 if i and j are equal and 0 if otherwise. """
		return 1 if i == j else 0

	@staticmethod
	def identity_matrix(n):
		""" Returns the identity matrix of a given dimension. """
		return LinAlg.matrix(n, n, lambda i, j: 1 if i == j else 0) if 0 < n else None	# Alternatively, use is_diagonal

	@staticmethod
	def multiply(A, B):
		""" Returns the product of two matrices or a matrix and a vector (in that
		order). The number of columns in A must equal the number of rows in B. """
		return [LinAlg.multiply_vectors(LinAlg.row(A, i), LinAlg.column(B, i)) for i in range(LinAlg.shape(A)[1])] if LinAlg.shape(A)[1] == LinAlg.shape(B)[0] else None

	# TODO
	@staticmethod
	def determinent(A):
		""" Returns the determinent of a matrix. """
		shape = LinAlg.shape(A)
		if shape[0] == shape[1]:
			d = 1
			if 1 < shape[0]:
				for i in range(shape[0]):
					d *= LinAlg.cofactor(A, i, i)
			elif shape[0] == 1:
				d = A[0][0]
		return d

	@staticmethod
	def cofactor(A, i, j):
		""" Returns the [i][j]th cofactor of matrix A. """
		return ((-1) ** j) * A[i][j] * LinAlg.determinent(LinAlg.submatrix(A, i, j))

	@staticmethod
	def submatrix(A, i, j):
		""" Returns the submatrix of A with the ith row and jth column removed. """
		shape = LinAlg.shape(A)
		B = LinAlg.matrix(shape[0], shape[1], lambda a, b: A[a][b])
		B.remove(i)
		for a in range(shape[0]):
			B[a].remove(j)
		return B

def main():
	""" A is a graph of connections between friends. B represents the same
	information but as an adjacency matrix rather than a list of edges. """
	A = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
	max_id = max(A, key=lambda a: a[0])[0]	# find the maximum a[0] in each tuple a = (x, y) of A
	B = LinAlg.matrix(max_id, max_id, lambda i, j: 1 if (i, j) in A else 0)
	print(B)

#main()
