import pandas as pd
from sklearn.tree import DecisionTreeClassifier

melbourne_data = pd.read_csv('melb_data.csv')

b= melbourne_data.describe()
a =melbourne_data.head()

# mean - середнє арифметичне
#std - стандартне відхилення

print(melbourne_data.columns)

# remove empty data
melbourne_data = melbourne_data.dropna(axis=0)

# ціль для прогнозування
y = melbourne_data.Price

# parameters
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]


melbourne_model = DecisionTreeClassifier(random_state=1)
melbourne_model.fit(X, y)


# функція передбачення
print(melbourne_model.predict(X.head()))
print("Первинне значення цін є такими:")
print(y.head())

melbourne_features2 = [ 'Rooms', 'Bathroom', 'Landsize']
X2 = melbourne_data[melbourne_features2]

model = DecisionTreeClassifier(random_state=1)
model.fit(X2,y)

print(model.predict(X2.head()))
print(y.head())

