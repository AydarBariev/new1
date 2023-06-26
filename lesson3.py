print("Введите  точку номер один")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))
x_diff = x1 - x2
y_diff = y1 - y2
k = y_diff / x_diff
b = y2 - k * x2
print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)
def count_number_len(x):
  count = 0
  while x:
    count += 1
    x //= 10
  return count
x = 1234
print(count_number_len(x))
y = 6
z = y - 5



