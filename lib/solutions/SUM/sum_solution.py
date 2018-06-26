# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
	if not isinstance(x, int) or not isinstance(y, int):
		raise TypeError("Parameters need to be of type 'INT'")
	return x + y
