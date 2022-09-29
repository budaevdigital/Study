"""
Несколько примеров из функционального программирования.
Каррирование, замыкание и т.д. 
"""

def adder(n):
    def fn(m):
        return n + m
    return fn

# То же самое, что и функция сверху
adder2 = lambda n: lambda m: n + m

sum = adder2(5)
print(sum(10))


def power_generator(exp):
    return lambda base: pow(base, exp)

square = power_generator(2)

# 4 в степени 2
print(square(4)) # 16

cube = power_generator(3)

# 6 в степени 3
print(cube(6)) # 216