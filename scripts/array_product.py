# https://www.geeksforgeeks.org/a-product-array-puzzle/

def array_product(inp):
    n = len(inp)
    res = [1] * n
    left = [1] * n
    right = [1] * n
    for i in range(1, n):
        left[i] = left[i-1] * inp[i - 1]
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * inp[i + 1]
    for i in range(n):
        res[i] = left[i] * right[i]
    return res


print(array_product([10, 3, 5, 6, 2]))
print(array_product([-1, 1, 0, -3, 3]))
