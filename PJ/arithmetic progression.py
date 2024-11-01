# Функція для розрахунку суми арифметичної прогресії
def arithmetic_sum(a1, d, n):
    total_sum = 0  # Ініціалізуємо суму
    current_term = a1  # Початковий член прогресії
    
    # Цикл для підрахунку суми
    for i in range(n):
        total_sum += current_term  
        current_term += d  
    
    return total_sum

a1 = float(input("Введіть перший член прогресії (a1): "))
d = float(input("Введіть різницю прогресії (d): "))
n = int(input("Введіть кількість членів прогресії (n): "))

# Результат
sum_result = arithmetic_sum(a1, d, n)
print(f"Сума перших {n} членів арифметичної прогресії: {sum_result}")
