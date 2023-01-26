import random

data = open('Data.csv','w')
data.write("ID,Weight,Revenue,X_loc,Y_loc\n")

amount_of_item=100
min_weight=2
max_weight=10
min_revenue=10
max_revenue=300
map_size=50

random.seed(1)

for i in range(100):
    Weight=str(random.randint(min_weight, max_weight))
    Revenue =str( random.randint(min_revenue, max_revenue))
    X_loc=str(random.randint(0, map_size))
    Y_loc =str( random.randint(0, map_size))

    data.write(str(i)+","+Weight+","+Revenue+","+X_loc+","+Y_loc+"\n")




