# Данный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создание пустых списков для простых и не простых чисел
primes = []
not_primes = []

# Перебор каждого числа из списка numbers
for num in numbers:
    if num < 2:  # Пропускаем числа меньше 2, так как 1 не простое
        not_primes.append(num)
        continue

    is_prime = True  # Предполагаем, что число простое

    # Вложенный цикл для проверки делителей
    for i in range(2, int(num**0.5) + 1):  # Делаем проверку до корня из числа
        if num % i == 0:  # Если остаток от деления равен 0, то число составное
            is_prime = False
            not_primes.append(num)
            break  # Прерываем цикл, так как нашли делитель

    if is_prime:  # Если остались с флагом is_prime = True, добавляем в primes
        primes.append(num)

# Выводим списки простых и не простых чисел
print("Primes:", primes)
print("Not Primes:", not_primes)