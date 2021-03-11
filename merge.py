"""
Comment.
"""


def factorial(upper_bound):
    if upper_bound == 0:
        return 1
    else:
        return upper_bound * factorial(upper_bound -1)


def main():
    """
    Drive the program.
    """
    print(factorial(10))


if __name__ == "__main__":
    main()
