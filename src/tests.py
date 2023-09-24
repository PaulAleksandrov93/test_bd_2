from regressor import CustomDummyRegressor

def test_fracsum():
    regressor = CustomDummyRegressor(strategy="fracsum")
    X = [[1], [2], [3]]
    y1 = [0.5, 1.3, -0.8]
    y2 = [5, 3, -8]
    
    result1 = regressor.fracsum(X, y1)
    result2 = regressor.fracsum(X, y2)

    assert result1 == 0.0
    assert result2 == 0.0

test_fracsum()