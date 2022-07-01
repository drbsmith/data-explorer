"""! @file

Type testing functions

@package src
"""

def howManyInt(series):
	"""! go through values in the series and count how many successfully cast to int and retain the same value
	"""

	res = [s for s in series if str(s).lstrip('-').isdigit()]

	return len(res)

def howManyFloat(series):

	# can't use something handy in list comprehension as easily, so we use the try/except version:
	ct = 0
	for s in series:
		try:
			float(s)
			ct += 1
		except ValueError:
			pass

	return ct

def dateLike(series):
	"""! perform a number of tests to try and assess the "date likeness" of the data in the series.

	-or- could throw some ML at it, right? but we have a deterministic function to try and cast it to datetime.
	"""
	ct = 0
	
