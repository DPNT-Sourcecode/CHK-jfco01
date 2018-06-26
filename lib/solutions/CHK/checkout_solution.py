

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    raise NotImplementedError()

def process_deal(sku, count, reg_price):
	"""
	Get the number of times a discount applies, and remainder, use that to calculate
	the final price of that sku.
	"""
	# Hardcoded rules here..
	if sku == "A" and count > 3:
		numdiscounts = count / 3
		remainder = count % 3
		return (numdiscounts * 130) + (remainder * reg_price)
	elif sku == "B" and count > 2:
		numdiscounts = count / 2
		remainder = count % 2
		return (numdiscounts * 45) + (remainder * reg_price)
	else:
		return count * reg_price


print(process_deal("B", 7, 30))