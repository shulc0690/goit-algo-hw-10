import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Визначення функції
def f(x):
    return x**2


# Метод Монте-Карло для обчислення інтеграла
a = 0
b = 2
N = 100000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

under_curve = y_random < f(x_random)
monte_carlo_value = (b - a) * (f(b)) * np.sum(under_curve) / N

# Аналітичний розрахунок
analytical_value = (b**3) / 3

# Використання функції quad
quad_value, _ = quad(f, a, b)

print(f"Значення інтеграла методом Монте-Карло: {monte_carlo_value:.4f}")
print(f"Аналітичне значення інтеграла: {analytical_value:.4f}")
print(f"Значення інтеграла за допомогою quad: {quad_value:.4f}")

# Створення графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, "r", linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()
