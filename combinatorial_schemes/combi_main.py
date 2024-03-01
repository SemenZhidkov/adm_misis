
# Жидков Семён, Зебелян Артем, Левченко Богдан, Ковалева Мария - БПМ-22-3

import math

#перестановки с повторениями

def permutation_with_repetition(multiset):
  sum = 0
  factorial_p = 1
  factorial_q = 1


  for element in multiset:
    sum += element

    for i in range(element):
      factorial_q *= (i + 1)

  for i in range(sum):
    factorial_p *= (i + 1)

  
  return int(factorial_p / factorial_q)

# тест:
A = [2, 1, 1, 2]  
print("Задача: \n Сколько существует различных перестановок из букв слова «Уссури»?\n Ответ: 180")  
print("Результат работы программы:")
print(permutation_with_repetition(A))

#перестановки без повторений
def permutation_of_n(n):
  factorial_n = 1
  for i in range(n):
      factorial_n *= (i + 1)
  return factorial_n

#тест
n = 8
print("Задача: \n Сколькими способами можно расположить на шахматной доске 8 ладей, чтобы они «не били» друг друга?\n Ответ: 8! = 40320")  
print("Результат работы программы:")
print(permutation_of_n(n))

# Сочетания без повторений
def combination_k_of_n(k: int, n: int) -> int:
  factorial_n = 1
  factorial_k = 1
  factorial_n_k = 1
  for i in range(n):
    factorial_n *= (i + 1)
    if i < (n - k):
      factorial_n_k *= (i + 1)
    
    if i < k:
      factorial_k *= (i + 1) 
  return int(factorial_n / (factorial_k * factorial_n_k))
      
#тест
print("Задача: \n В ящике находится 15 деталей. Сколькими способами можно взять 4 детали?\n Ответ: 1365")  
print("Результат работы программы:")
print(combination_k_of_n(4, 15))

# Сочетания с повторениями
def combination_with_repetition(m: int, n: int) -> int:
  factorial_n_m_1 = 1
  factorial_n_1 = 1
  factorial_m = 1
  for i in range(n + m - 1):
    factorial_n_m_1 *= (i + 1)
    if i < (n - 1):
      factorial_n_1 *= (i + 1)
    
    if i < m:
      factorial_m *= (i + 1) 
  return int(factorial_n_m_1 / (factorial_n_1 * factorial_m))
      
#тест
print("Задача: \n В студенческой столовой продают сосиски в тесте, ватрушки и пончики. Сколькими способами можно приобрести пять пирожков?\n Ответ: 21")  
print("Результат работы программы:")
print(combination_with_repetition(5, 3))
print("\nПриятного аппетита!")




# Правило суммы
def sum_rule(*args):
    """
    Реализует правило суммы комбинаторики.
    
    Аргументы:
    *аргументы: Переменное количество аргументов, представляющих количество различных событий.
    
    Возвращается:
    int: Сумма отсчетов всех событий.
    """
    return sum(args)


# Тестируем функцию различными значениями 
print(sum_rule(2, 3, 4))  # 2 + 3 + 4 = 9
print(sum_rule(10, 20, 30, 40))  # 10 + 20 + 30 + 40 = 100
print(sum_rule(0, 0, 0, 0))  # 0 + 0 + 0 + 0 = 0
print(sum_rule(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Сумма первых 10 натуральных чисел = 55 
        
def direct_product_rule(*args):
    """
    Реализует правило прямого произведения комбинаторики.
    
    Аргументы:
    *args: Переменное количество аргументов, представляющих количество различных событий.
    
    Возвращается:
    int: Результат подсчета всех событий.
    """
    return math.prod(args)

# Test the function with different values
print(direct_product_rule(2, 3, 4))  # 2 * 3 * 4 = 24
print(direct_product_rule(10, 20, 30, 40))  # 10 * 20 * 30 * 40 = 240000
print(direct_product_rule(0, 0, 0, 0))  # 0 * 0 * 0 * 0 = 0
print(direct_product_rule(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Произведение первых 10 чисел натурального ряда = 3628800

import unittest

def factorial(x: int):
    if x in (0, 1):
        return 1
    return x * factorial(x - 1)
    

def permutations_with_reps(n: int, m: int):
    return pow(n, m)


def permutations_without_reps(n: int, m: int):
    return factorial(n) / factorial(n - m)

def factorial(x: int) -> int:
    if x in (0, 1):
        return 1
    return x * factorial(x - 1)
    

def permutations_with_reps(n: int, m: int) -> int:
    return pow(n, m)


def permutations_without_reps(n: int, m: int) -> int:
    return factorial(n) / factorial(n - m)


class PermutationsTests(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)


    def test_perm_with_reps(self):
        self.assertEqual(
            permutations_with_reps(2, 4), 16,
        )
        self.assertEqual(
            permutations_with_reps(3, 5), 243,
        )

    def test_perm_without_reps(self):
        self.assertAlmostEqual(
            permutations_without_reps(10, 2), 90
        )
        self.assertAlmostEqual(
            permutations_without_reps(15, 2), 210
        )

if __name__ == '__main__':
    unittest.main()