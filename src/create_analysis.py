"""! @file

Create Feature Analysis

@package src """


import os,sys
p = os.path.abspath('./src')
sys.path.append(p)

if __name__ == "__main__":
	import pandas as pd

	df = pd.read_csv(sys.argv[1])

	import DataFrame
	de = DataFrame.DataExploder(df)

	logic = de.allLogicTests()
	text = de.allTextTests()
	stats = de.allStatisticTests()

	df_out = pd.DataFrame(logic).set_index('label')
	df_out = df_out.join(pd.DataFrame(text).set_index('label'))
	df_out = df_out.join(pd.DataFrame(stats).set_index('label'))

	print(df_out.head())

	fname = sys.argv[1][:sys.argv[1].find('.')]

	fname = fname[- fname[::-1].find('/') : ]

	df_out.to_csv('./tmp/{}_features.csv'.format(fname))
