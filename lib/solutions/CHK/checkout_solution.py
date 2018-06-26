import string

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	# Check is STR
	try:
		skus = unicode(skus, "utf-8")
	except TypeError:
		skus = skus

	if not isinstance(skus, unicode):
		return -1

	# Check if valid sku
	for sku in skus:
		if sku not in "ABCD":
			return -1
	# Check no punct
	for sku in skus:
		if sku in string.punctuation:
			return -1

	if skus == None:
		return -1

	cart_value = 0
	def process_skus(sku, val, skus):
		if sku in skus:
			return process_deal(sku, skus.count(sku), val)
		else:
			return 0

	for k, v in {"A":50, "B":30, "C":20, "D":15, "E":40}.items():
		cart_value += process_skus(k, v, skus)

	return cart_value

def process_deal(sku, count, all_skus):
	"""
	Get the number of times a discount applies, and remainder, use that to calculate
	the final price of that sku.
	"""
	inventory = {"A":50, "B":30, "C":20, "D":15, "E":40}

	if sku == "A" and count >= 3 and count <5:
		numdiscounts = count / 3
		remainder = count % 3
		return (numdiscounts * 130) + (remainder * inventory["A"])
	elif sku == "A" and count >= 5:
		numdiscounts = count / 5
		remainder = count % 5 
		return (numdiscounts * 200) + (remainder * inventory["A"])
	elif sku == "E":
		if count < 2:
			return count * inventory["E"]
		elif count >= 2 and "B" in all_skus:
			numdiscounts = count / 2
			b_count = all_skus.count("B")
			# 'get b count then check how many of those are free'

			free = b_count - numdiscounts
			print(b_count, numdiscounts)

			return (inventory["E"] * count) - ((inventory["B"] * b_count))
		elif count >= 2 and "B" not in all_skus:
			return inventory["E"] * count
	elif sku == "B" and count >= 2:
		numdiscounts = count / 2
		remainder = count % 2
		return (numdiscounts * 45) + (remainder * inventory["B"])
	elif sku == "C":
		return count * inventory["C"]
	elif sku == "D":
		return count * inventory["D"]
	else:
		return 0


print(process_deal("E", 6, "EEEEEBBBB"))
print(6 % 3)
