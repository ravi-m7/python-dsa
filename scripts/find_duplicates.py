# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

def find_duplicate(input):
    mem = []
    for i in input:
        if i in mem:
            print(i, " is duplicate")
        else:
            mem.append(i)


find_duplicate([1, 2, 3, 6, 3, 6, 1])
find_duplicate([1, 2, 4, 5, 6])
