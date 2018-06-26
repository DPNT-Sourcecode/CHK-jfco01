

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(string):
	if not isinstance(string, str):
		raise TypeError("Parameter must be a string.")
	return "Hello, {}!".format(string)