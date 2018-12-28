# V76 Doctest

def areaTriangulo(base,altura):
	"""
		Calcula el area de un triangiulo dada su base y altura

		>>> areaTriangulo(3,6)
		9.0
	"""
	return (base*altura)/2

print(areaTriangulo(2,4))


import doctest
doctest.testmod()

