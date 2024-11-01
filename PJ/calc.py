# Функція для додавання
def add(x, y):
    return x + y

# Функція для віднімання
def subtract(x, y):
    return x - y

# Функція для множення
def multiply(x, y):
    return x * y

# Функція для ділення
def divide(x, y):
    if y == 0:
        return "Помилка: ділення на нуль!"
    return x / y

# Основна програма
print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

while True:
    # Отримуємо вибір операції від користувача
    choice = input("Введіть номер операції (1/2/3/4): ")

    # Перевірка на правильний ввід
    if choice in ('1', '2', '3', '4'):
        # Отримуємо два числа від користувача
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        # Виконуємо обрану операцію
        if choice == '1':
            print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")

        # Запитуємо, чи хоче користувач продовжити
        next_calculation = input("Хочете виконати ще одну операцію? (так/ні): ")
        if next_calculation.lower() != 'так':
            break
    else:
        print("Неправильний ввід, спробуйте ще раз.")
