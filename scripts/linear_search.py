input_list = [15, 14, 9, 4, 46, 43, 29]
search_val = 4

# Find the index of an element from a list of element
# Brute Force


def find_number(inp_list, val):
    for i, j in enumerate(inp_list):
        if val == j:
            return i
    return -1


def find_number1(inp_list, val):
    for i in range(len(inp_list)):
        if val == inp_list[i]:
            return i
    return -1


print(find_number(input_list, search_val))
print(find_number1(input_list, search_val))
