import numpy as np

data = open('Data.csv', 'w')
data.write("ID,Weight,Revenue,X_loc,Y_loc\n")

amount_of_item = 50
min_weight = 2
max_weight = 10
min_revenue = 10
max_revenue = 300
map_size = 50

np.random.seed(1)

weights = np.random.randint(min_weight, max_weight + 1, size=amount_of_item)
revenues = np.random.randint(min_revenue, max_revenue + 1, size=amount_of_item)
x_locs = np.random.randint(0, map_size, size=amount_of_item)
y_locs = np.random.randint(0, map_size, size=amount_of_item)

for i in range(amount_of_item):
    Weight = str(weights[i])
    Revenue = str(revenues[i])
    X_loc = str(x_locs[i])
    Y_loc = str(y_locs[i])

    data.write(str(i) + "," + Weight + "," + Revenue + "," + X_loc + "," + Y_loc + "\n")
