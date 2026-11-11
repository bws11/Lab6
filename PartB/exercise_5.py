def minimum(lst: list):
    a = 999
    for x in range(1, len(lst)):

        if lst[x] < a:
            a = lst[x]
    return a

