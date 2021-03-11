"""
Comment.
"""


def factorial(upper_bound):
    product = 1
    for number in range(1, upper_bound + 1):
        product *= number
    return product


def main():
    """
    Drive the program.
    """
    print(factorial(5))


if __name__ == "__main__":
    main()
