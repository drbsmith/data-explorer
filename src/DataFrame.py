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

	# TODO: mad, max, mean, median, min, sem, skew, std, var, 
	# TODO maybe: mode, quantile .5, .95, .25, .75
	def kurtosis(self):
		ret = {}

		for col in self.df:
			try:
				ret[col] = self.df[col].kurtosis()
			except TypeError:
				ret[col] = None

		return ret

	def statistics(self):
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