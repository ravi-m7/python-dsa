# Find the index of an element from a list of element
# Input is sorted


def find_number(input_list, search_val):
    #print(input_list, search_val)
    low = 0
    high = len(input_list)

    while low <= high:
        mid = (low + high) // 2
        if len(input_list) == 0:
            return -1
        elif input_list[mid] == search_val:
            return mid
        elif input_list[mid] < search_val:
            low = mid + 1
        elif input_list[mid] > search_val:
            high = mid - 1
    return -1


test_cases = [
    {
        "input": {
            "input_list": [3, 4, 9, 14, 41, 43, 229],
            "search_val": 3},
        "output": 0
    },
    {"input": {
        "input_list": [3, 4, 9, 14, 41, 43, 229],
        "search_val": 229},
        "output": 6
    },
    {"input": {
        "input_list": [3, 4, 9, 14, 41, 43, 229],
        "search_val": 123},
        "output": -1
    },
    {"input": {
        "input_list": [],
        "search_val": 1},
        "output": -1
    }
]

for i in range(len(test_cases)):
    print(find_number(**test_cases[i]["input"]) == test_cases[i]["output"])

