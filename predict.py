from sklearn.linear_model import LinearRegression
import pandas as pd 

data = pd.read_csv('laptop_price.csv')

val1 = input("Inches : ")
val2 = input("Ram : ")

x_trainingData = data[['Inches', 'Ram']]
y_trainingData = data['Price_euros']

model = LinearRegression()
model.fit(x_trainingData, y_trainingData)

x_new = [[float(val1), int(val2)]]
calculation = model.predict(x_new)

print("A laptop that's " + val1 + " inches and has " + val2 + " GB of RAM costs " + str(calculation) + " euros.")
