x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]

m = 0
b = 0


def predict(x, m, b):
    return m * x + b


def mse(x, y, m, b):
    total = 0

    for i in range(len(x)):
        prediction = predict(x[i], m, b)
        error = y[i] - prediction
        total += error ** 2

    return total / len(x)


def gradients(x, y, m, b):
    dm = 0
    db = 0
    n = len(x)

    for i in range(n):
        prediction = predict(x[i], m, b)
        error = y[i] - prediction

        dm += -2 * x[i] * error
        db += -2 * error

    dm /= n
    db /= n

    return dm, db


learning_rate = 0.01
epochs = 1000

for epoch in range(epochs):

    dm, db = gradients(x, y, m, b)

    m = m - learning_rate * dm
    b = b - learning_rate * db

    if epoch % 100 == 0:
        print(f"Epoch {epoch} | Loss = {mse(x, y, m, b):.4f}")


print("\nEğitim tamamlandı.")
print(f"m = {m:.4f}")
print(f"b = {b:.4f}")

print("\nTest:")
print(f"x = 10 -> y = {predict(10, m, b):.2f}")