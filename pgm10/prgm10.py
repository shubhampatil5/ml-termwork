"""
10. Implement the non-parametric Locally Weighted Regression algorithm in order to
fit data points. Select appropriate data set for your experiment and draw graphs.
"""
import numpy as np
import matplotlib.pyplot as plt

tou = 0.5

X_train = np.array(list(range(3, 33)) + [3.2, 6.2])
print(X_train)
X_train = X_train[:, np.newaxis]
print(len(X_train))
y_train = np.array([1, 2, 1, 2, 1, 1, 3, 4, 5, 4, 1, 10, 6, 4, 4, 5, 7, 2, 8, 9, 1, 12, 10, 5, 7, 8, 3, 5, 2, 9, 10, 4])

X_test = np.array([i / 10 for i in range(400)])
X_test = X_test[:, np.newaxis]

y_test = []

count = 0
for r in range(len(X_test)):
    try:
        wts = np.exp(-np.sum((X_train - X_test[r]) ** 2, axis=1) / (2 * tou ** 2))
        W = np.diag(wts)
        factor1 = np.linalg.inv(X_train.T.dot(W).dot(X_train))
        parameters = factor1.dot(X_train.T).dot(W).dot(y_train)
        prediction = X_test[r].dot(parameters)
        y_test.append(prediction)
        count += 1
    except Exception as e:
        print(e)
        pass
print(len(y_test))
y_test = np.array(y_test)
plt.plot(X_train.squeeze(), y_train, 'o')

plt.plot(X_test.squeeze(), y_test, 'o')
plt.show()
