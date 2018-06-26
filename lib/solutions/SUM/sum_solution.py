# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
	if not isinstance(x, int) or not isinstance(y, int):
		raise TypeError("Parameters need to be of type 'INT'")
	if x < 0 or x > 100 or y < 0 or y > 100:
		raise ValueError("Provided integers must be between 0 and 100")
	return x + y
