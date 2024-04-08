import pandas as pd

url='https://es.wikipedia.org/wiki/Mazinger_Z'

extract = pd.read_csv(url)
print(len(extract))