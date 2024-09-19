import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# crear ejemplo
data ={
    'tamaño':[2000, 1500, 3500, 1900, 4000],
    'precio':[50000,30000,40000,60000, 200000]
}
df = pd.DataFrame(data)

#dividir los datos
x= df[['tamaño']]
y=df['precio']
x_train, x_test, y_train, y_test = train_test_split(x ,y, test_size=0.2, random_state=42)

# entrenar el model
model = LinearRegression()
model.fit(x_train, y_train)

# realizar predecciones
y_pred = model.predict(x_test)

#diagnosticar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f'MSE:{mse}')