import pulp

# Створюємо задачу лінійного програмування
prob = pulp.LpProblem("Maximize Drink Production", pulp.LpMaximize)

# Створюємо змінні для кількості вироблених напоїв
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Обмеження на ресурси
water = 100
sugar = 50
lemon_juice = 30
fruit_puree = 40

# Додаємо обмеження на використання ресурсів
prob += 2 * lemonade + 1 * fruit_juice <= water, "Water"
prob += 1 * lemonade <= sugar, "Sugar"
prob += 1 * lemonade <= lemon_juice, "LemonJuice"
prob += 2 * fruit_juice <= fruit_puree, "FruitPuree"

# Цільова функція - максимізувати загальну кількість вироблених напоїв
prob += lemonade + fruit_juice, "Total_Production"

# Розв'язуємо задачу
prob.solve()

# Виводимо результати
print("Status:", pulp.LpStatus[prob.status])
print("Lemonade produced:", pulp.value(lemonade))
print("Fruit Juice produced:", pulp.value(fruit_juice))
