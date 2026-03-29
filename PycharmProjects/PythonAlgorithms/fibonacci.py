def fibonacci_recurr(n):
    if n <= 1:
        return 1
    else:
        return fibonacci_recurr(n - 1) + fibonacci_recurr(n - 2)


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        prev = 1
        current = 1
        for i in range(2, n + 1):
            prev, current = current, prev + current

        return current


if __name__ == "__main__":
    print("Printing fibinacci")
    for i in range(11):
        res = fibonacci(i) #fibonacci_recurr(i)
        print(f"for i={i}: {res}")
