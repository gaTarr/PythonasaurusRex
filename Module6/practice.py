def binomial_coeff(n, k):
    """Compute the binomial coefficient for Pascal's Triangle"""
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res


def pascal_triangle(n):
    """Print first n lines of Pascal's Triangle"""
    # Iterate each line and print it
    for line in range(0, n):
        # Row (line) r has r elements
        for i in range(0, line + 1):
            print(binomial_coeff(line, i)," ", end="")
        print()

if __name__ == '__main__':
    try:
        n = int(input("Enter the number of rows to view of Pascal's Triangle:"))
    except ValueError as err:
        print("ValueError found!!")
    else:
        pascal_triangle(n)
