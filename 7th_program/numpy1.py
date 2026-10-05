import pandas as pd

df = pd.DataFrame({'Sales':[100,200,150,300,250]})
print("Maximum:", df.Sales.max())
print("Minimum:", df.Sales.min())