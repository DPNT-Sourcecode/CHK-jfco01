

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
	if not isinstance(friend_name, str):
		raise TypeError("Parameter must be a string.")
	if friend_name is "":
		raise ValueError("Name parameter cannot be blank")
	return "Hello, {}!".format(friend_name)
