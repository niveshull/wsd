import pandas as pd

df = pd.read_csv('elexis-wsd-1.0/elexis-wsd-sl_sense-inventory.tsv', sep='\t', header=None, names=['word', 'sentence', 'sense_ids'])

print(df)