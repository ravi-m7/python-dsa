input_list = [15, 14, 9, 4, 46, 43, 29]
output = 4

# Find the index of an element from a list of element
# Brute Force


def find_number(inp_list, val):
    for i, j in enumerate(inp_list):
        if val == j:
            return i
    return -1


def find_number1(inp_list, val):
    for i in range(len(input_list)):
        if output == input_list[i]:
            return True
            break
    return False


print(find_number(input_list, output))
print(find_number1(input_list, output))
