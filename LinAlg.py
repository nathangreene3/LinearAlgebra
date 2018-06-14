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
		return add_vectors(u, scalar_multiply(-1, v))

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
		return sum(multiply_vectors(u, v))

	@staticmethod
	def mean_vector(V):
		""" Returns a vector with each ith component being the mean value of the
		ith components of the set of vectors. """
		return scalar_multiply(1 / len(V), sum(V))

	@staticmethod
	def sum_squares(v):
		""" Returns the sum of the squared components of a vector. """
		return dot_product(v, v)

	@staticmethod
	def squared_difference(u, v):
		""" Returns a vector with components being the squared difference
		between two given vectors. """
		return sum_squares(subtract_vectors(u, v))

	@staticmethod
	def distance(u, v):
		""" Returns the Euclidean distance between two vectors. """
		return math.sqrt(squared_difference(u, v))

	@staticmethod
	def magnitude(v):
		""" Returns the magnitude of a vector. """
		return math.sqrt(dot(v, v))

	@staticmethod
	def shape(A):
		""" Returns the number of rows and columns in a matrix as a tuple. """
		return len(A), len(A[0]) if A else 0

	@staticmethod
	def row(A, i):
		""" Returns the ith row in matrix A. """
		return A[i]

	@staticmethod
	def column(A, i):
		""" Returns the ith column in matrix A. """
		return [row[j] for row in A]

	@staticmethod
	def matrix(m, n, fn):
		""" Returns an m x n matrix with entries defined by the function fn. """
		return [[fn(i, j) for j in range(n)] for i in range(m)]

	@staticmethod
	def is_diagonal(i, j):
		return 1 if i == j else 0

	@staticmethod
	def identity_matrix(n):
		""" Returns the identity matrix of a given dimension. """
		return matrix(n, n, lambda i, j: 1 if i == j else 0) if 0 < n else None	# Alternatively, use is_diagonal

	@staticmethod
	def multiply(A, B):
		""" Returns the product of two matrices or a matrix and a vector (in that order). The number of columns in A must equal the number of rows in B. """
		return [multiply_vectors(row(A, i), column(B, i)) for i in range(shape(A)[1])] if shape(A)[1] == shape(B)[0] else None

def main():
	""" A is a graph of connections between friends. B represents the same
	information but as an adjacency matrix rather than a list of edges. """
	A = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
	max_id = max(A, key=lambda x: x[0])[0]	# find the maximum x in each (x, y)
	B = LinAlg.matrix(max_id, max_id, lambda i, j: 1 if (i, j) in A else 0)
	print(B)

main()
