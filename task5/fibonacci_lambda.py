from functools import reduce

fib_numbers = lambda y: reduce(lambda x, _: x + [x[-1] + x[-2]], range(y - 2), [0, 1])

n = int(input("Enter a N value for fibonacci sequence: "))
print(fib_numbers(n))