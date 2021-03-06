



import os,sys
p = os.path.abspath('./src')
sys.path.append(p)

from DataFrame import DataExploder



if __name__ == '__main__':
	import pandas as pd

	df = pd.read_csv('~/Downloads/2022-0201-0327-inbox-data-export.jby5aft8.32da9fe7-188b-4bbb-a105-9fa2755cfb74.csv')

	de = DataExploder(df)

	print('**** text tests:')
	print(pd.DataFrame(de.allTextTests()))

	# to make these better tests, check the results, using a test .csv that we know the results of.
	print('**** Unique:')
	print(de.unique())

	print('**** Missing:')
	print(de.missing())

	print('**** Ints?:')
	print(de.int())
	print('**** Floats?:')
	print(de.float())

	print('**** statistics:')
	dg = de.allStatisticTests()
	print(pd.DataFrame(dg))