
# Задача А

from src.regressor import CustomDummyRegressor


regressor = CustomDummyRegressor(strategy="fracsum")
X = [[1], [2], [3]]
y1 = [0.5, 1.3, -0.8]
y2 = [5, 3, -8]

result1 = regressor.fracsum(X, y1)
result2 = regressor.fracsum(X, y2)

print(result1)  
print(result2)  