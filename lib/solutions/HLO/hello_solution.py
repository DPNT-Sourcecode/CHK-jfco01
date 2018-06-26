

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(string):
	if not isinstance(string, str):
		raise TypeError("Parameter must be a string.")
	if string is "":
		raise ValueError("Name parameter cannot be blank")
	return "Hello, {}!".format(string)