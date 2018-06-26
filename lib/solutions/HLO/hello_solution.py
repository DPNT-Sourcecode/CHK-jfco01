

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
	if not isinstance(friend_name, str):
		raise TypeError("Parameter must be a string.")
	return "Hello, {}!".format(friend_name)
