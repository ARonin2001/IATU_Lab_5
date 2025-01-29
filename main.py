"""
	F(1) = 1, F(2) = 1, F(n) = (-1)n*(F(n-2)/(2n)!), при n > 2
	Задана рекуррентная функция. Область определения функции – натуральные числа. 
	Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной форме. 
	Обязательное требование – минимизация времени выполнения и объема памяти.
"""

import time

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return None  # Возвращаем None для обозначения ошибки

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def factorial_2n():
    result_factorial = None

    def fact(n):
        nonlocal result_factorial
        
        n_fact = 2 * n
        if result_factorial is None:
            result_factorial = factorial(n_fact)
        else:
            result_factorial *=  (n_fact - 1) * n_fact

        return result_factorial
    
    return fact

def recursive_f(n):
    if n < 1:
        return "Недопустимое значение n!"
    if n < 3:
        return 1
    else:
        factorial_func_2n = factorial_2n()
        try:
            fn_minus_2 = recursive_f(n - 2) if n > 2 else 1

            result_factorial = factorial_func_2n(n) #вычисление факториала
            if result_factorial is None:
                 return "Факториал определен только для неотрицательных чисел" #Возвращаем ошибку

            minus_1_degree = 1 if n % 2 == 0 else -1
            return minus_1_degree * (fn_minus_2 / result_factorial)
        except ZeroDivisionError:
           return "Деление на ноль!"

def iterative_f(n):
    if n < 1:
        return "Недопустимое значение n!"
    if n < 3:
        return 1
    else:
        F_prev_prev = 1  # F(0)
        F_prev = 1       # F(1)
        factorial_func_2n = factorial_2n()
        for i in range(3, n + 1):
            result_factorial = factorial_func_2n(i)
            minus_1_degree = 1 if i % 2 == 0 else -1

            F_current = minus_1_degree * (F_prev_prev / result_factorial)
            F_prev_prev = F_prev
            F_prev = F_current
        return F_prev

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
