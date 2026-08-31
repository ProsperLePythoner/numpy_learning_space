from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100, 3)
y = 3*x[:,0] + 2*x[:,1] + x[:,2] + np.random.randn(100) * .1

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Lasso Regression": Lasso(alpha=.1),
}

for name, model in models.items():
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print(name, "MSE: ", mean_squared_error(y_test, y_pred))
