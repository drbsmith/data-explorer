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