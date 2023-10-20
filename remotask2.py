def binary_exponentiation(base, exponent):
    if exponent >= 0:
        # Base case: if exponent is 0, return 1
        if exponent == 0:
            return 1
        # Recursive case: if exponent is even
        elif exponent % 2 == 0 and exponent > 0:
            result = binary_exponentiation(base, exponent // 2)
            return result * result
        # Recursive case: if exponent is odd
        else:
            result = binary_exponentiation(base, (exponent - 1) // 2)
            return base * result * result
    else:
        print("Please provide a valid input.")


base = 3
exponent = 13
print(binary_exponentiation(base, exponent))


# Use this Python environment to write and test your Python code responses for Turns 1-3
# Please ensure your Turn 2 and Turn 3 Responses compile and are correct before copying code from this environment and pasting it into Remotasks. Thank you!
# def binary_exponentiation(base, exponent):
#     if exponent >= 0:
#         # Base case: if exponent is 0, return 1
#         if exponent == 0:
#             return 1
#         # Recursive case: if exponent is even
#         elif exponent % 2 == 0 and exponent > 0:
#             result = binary_exponentiation(base, exponent // 2)
#             return result * result
#         # Recursive case: if exponent is odd
#         else:
#             result = binary_exponentiation(base, (exponent - 1) // 2)
#             return base * result * result
#     else:
#         print("Please provide a valid input.")


def binary_exponentiation(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    pow = 1
    while exponent:
        if exponent & 1:
            pow *= base
        base *= base
        exponent >>= 1
    return pow


base = 3
exponent = 13
print(binary_exponentiation(base, exponent))


class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


# Iterative:


class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
