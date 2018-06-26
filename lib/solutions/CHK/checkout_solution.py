

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    raise NotImplementedError()

def is_deal(sku, count):
	# Hardcoded rules here..
	if sku == "A" and count > 3:
		numdiscounts = count / 3
		return numdiscounts
	elif sku == "B" and count > 2:
		pass
	else:
		return False


print(is_deal("A", 7))