

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	cart_value = 0
	def process_skus(sku, val, skus):
		if sku in skus:
			return process_deal(sku, skus.count(sku), val)
		else:
			return 0

	for k, v in {"A":50, "B":30, "C":20, "D":15}.items():
		cart_value += process_skus(k, v, skus)

	return cart_value

def process_deal(sku, count, reg_price):
	"""
	Get the number of times a discount applies, and remainder, use that to calculate
	the final price of that sku.
	"""
	# Hardcoded rules here..
	if sku == "A" and count >= 3:
		numdiscounts = count / 3
		remainder = count % 3
		return (numdiscounts * 130) + (remainder * reg_price)
	elif sku == "B" and count >= 2:
		numdiscounts = count / 2
		remainder = count % 2
		return (numdiscounts * 45) + (remainder * reg_price)
	else:
		return count * reg_price
