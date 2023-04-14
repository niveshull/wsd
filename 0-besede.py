import pandas as pd

df = pd.read_csv('/home/nives/Projekti/ONJ-p/elexis-wsd-1.0/sense_inventories/elexis-wsd-sl_sense-inventory.tsv', sep='\t', header=None, names=['word', 'sentence', 'sense_ids'])

print(df)