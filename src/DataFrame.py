"""! @file

Data Frame

@package src
"""

import pandas as pd

class DataExploder:
	def __init__(self, data):
		if type(data) is pd.DataFrame:
			self.df = data
		else:
			self.df = pd.DataFrame(data)

	def unique(self):
		"""! check each column for the % of unique values.
		"""
		unique = {}
		percent = {}
		for col in self.df:
			unique[col] = self.df[col].unique()
			percent[col] = len(unique[col]) / len(self.df[col])

		return percent

	def missing(self):
		"""! calculate percentage of values missing (na) in each column
		"""
		percent = {}
		for col in self.df:
			percent[col] = 1.0 - (len(self.df[col].dropna()) / len(self.df[col]))

		return percent

	def int(self):
		from TypeHypotheses import howManyInt

		percent = {}
		for col in self.df:
			percent[col] = howManyInt(self.df[col].dropna()) / len(self.df[col])

		return percent
	def float(self):
		from TypeHypotheses import howManyFloat

		percent = {}
		for col in self.df:
			percent[col] = howManyFloat(self.df[col].dropna()) / len(self.df[col])

		return percent

	def allLogicTests(self):

		ret = []

		uni = self.unique()
		miss = self.missing()
		notreal = self.int()
		real = self.float()

		for col in self.df:
			entry = {'label': col}
			entry['unique'] = uni[col]
			entry['missing'] = miss[col]
			entry['real-numbers'] = real[col]
			entry['integers'] = notreal[col]

			ret.append(entry)

		return ret

	def allStatisticTests(self):
		"""! does: 
		* mad, max, mean, median, min, sem, skew, std, var, kurtosis, mode
		"""
		# TODO maybe: mode, quantile .5, .95, .25, .75
		ret = []

		for col in self.df:
			x = self.df[col]

			entry = {'label': col}

			try:
				entry['max'] = x.max()
				entry['min'] = x.min()
				entry['mean'] = x.mean()
				entry['median'] = x.median()
				entry['std'] = x.std()
				entry['var'] = x.var()
				entry['mad'] = x.mad()
				entry['sem'] = x.sem()
				entry['skew'] = x.skew()
				entry['kurtosis'] = x.kurtosis()
				entry['mode'] = x.mode()
			except TypeError:
				pass # it can't be cast to numeric

			ret.append(entry)

		return ret

	def allTextTests(self):
		"""! run all of the string/text tests we have come up with. """
		from data_exploder_util import _unique_char, _unique_punc, _unique_digits, _unique_hexdigits

		ret = []
		for col in self.df:
			# cast each to string, maybe it's the best interpretation?
			length = self.df[col].astype("string")

			entry = {'label': col}
			entry['len-max'] = length.str.len().max()
			entry['len-min'] = length.str.len().min()
			entry['len-median'] = length.str.len().median()
			entry['len-mean'] = length.str.len().mean()

			# how to think about unique characters? A deep scan would look through each entry, but that would be slow in big sets and does it tell us that much? 
			# options: 
			# * deep scan to create the set of characters in the column
			# * get the number of unique characters in each entry, then stats on those
			# * want to know how many are in: letters, numbers, symbols, punctuation, ...
			length = length.dropna()
			sets = length.apply(_unique_char)
			entry['unique-char-mean'] = sets.mean()
			entry['unique-char-max'] = sets.max()
			entry['unique-char-min'] = sets.min()

			sets = length.apply(_unique_punc)
			entry['unique-punc-mean'] = sets.mean()
			sets = length.apply(_unique_digits)
			entry['unique-digits-mean'] = sets.mean()
			sets = length.apply(_unique_hexdigits)
			entry['unique-hexdigits-mean'] = sets.mean()

			ret.append(entry)

		return ret
