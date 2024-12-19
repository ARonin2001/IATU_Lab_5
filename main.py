"""
	F(1) = 1, F(2) = 1, F(n) = (-1)n*(F(n-2)/(2n)!), при n > 2
	Задана рекуррентная функция. Область определения функции – натуральные числа. 
	Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной форме. 
	Обязательное требование – минимизация времени выполнения и объема памяти.
"""

import time
import math

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return None  # Возвращаем None для обозначения ошибки
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def recursive_f(n):
    if n > 1000:
        return None

    if n < 3:
        return 1
    else:
        try:
            fact_val = factorial(2 * n) # Факториал вычисляется для 2*n
            if fact_val is None:
                 return "Факториал определен только для неотрицательных чисел" #Возвращаем ошибку
            return (-1)**n * (recursive_f(n - 2) / fact_val)
        except ZeroDivisionError:
           return "Деление на ноль!"

def iterative_f(n):
    if n > 1000:
        return None
    if n < 1:
        return "Недопустимое значение n!"
    if n < 3:
        return 1
    else:
        f_n_minus_2 = 1  # F(1) и F(2) = 1
        f_n_minus_4 = 1
        f_n = 0
        for i in range(3, n + 1):
           try:
                fact_val = factorial(2 * i)
                if fact_val is None:
                    return "Факториал определен только для неотрицательных чисел"
                f_n = (-1) ** i * (f_n_minus_2 / fact_val)

                f_n_minus_4 = f_n_minus_2  # Сохраняем предыдущий F(n-2)
                f_n_minus_2 = f_n          # Текущее значение F(n)
           except ZeroDivisionError:
                 return "Деление на ноль!"
           except OverflowError:
                return "Переполнение!"

        return f_n


def compare_times(n_values):
    results = []
    for n in n_values:
        recursive_start = time.time()
        recursive_result = recursive_f(n)
        recursive_end = time.time()

        iterative_start = time.time()
        iterative_result = iterative_f(n)
        iterative_end = time.time()

        results.append([n,
                       recursive_end - recursive_start,
                       iterative_end - iterative_start,
                       recursive_result,
                       iterative_result])
    return results


def main():
    n_values = range(1, 10)
    results = compare_times(n_values)

    print("Результаты сравнения:")
    print("n\tРекурсивное время\tИтерационное время\tРезультат рекурсивный\tРезультат итерационный")
    for result in results:
        print(f"{result[0]}\t{result[1]:.6f}\t\t{result[2]:.6f}\t\t{result[3]}\t\t{result[4]}")


if __name__ == "__main__":
    main()