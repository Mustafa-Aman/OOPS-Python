import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


import pandas as pd

data = pd.read_csv("nba.csv", index_col="Name")
first = data["Number"]
print(first)
