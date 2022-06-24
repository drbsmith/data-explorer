"""! @file



@package src
"""

import string

def _unique_char(x):
	return len(set(x))

def _unique_punc(x):
	return len([c for c in set(x) if c in string.punctuation])

def _unique_digits(x):
	return len([c for c in set(x) if c in string.digits])
def _unique_hexdigits(x):
	return len([c for c in set(x) if c in string.hexdigits])