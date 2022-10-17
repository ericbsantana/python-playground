def cube(x): return x ** 3


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_list(n):
    f = []
    for i in range(0, n):
        f.append(fibonacci(i))
    return f


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci_list(n))))
