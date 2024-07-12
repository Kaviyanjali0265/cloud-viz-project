import pandas as pd

# read the data

data=pd.read_csv('data/iris.data' , header=None)

# convert to numerical values

data[4] = data[4].replace('Iris-setosa',0)
data[4] = data[4].replace('Iris-virginica',1)
data[4] = data[4].replace('Iris-versicolor',2)
data[4] = data[4].infer_objects(copy=False)

print(data)

# shuffle
data = data.sample(frac=1).reset_index(drop=True)

# change the label col index
data = data[[4,0,1,2,3]]

print(data)

#split (train,val sets)
# 80% train data
# 20% validation data

train_data = data[:120]
val_data = data[120:]
