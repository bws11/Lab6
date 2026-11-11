def find_common_elements(a: list, b: list) -> list:
    in_both: list = []
    a, b = list(set(a)), list(set(b))
    for i in range(len(a)):
        if a[i] in b:
            in_both.append(a[i])

    return sorted(in_both) if in_both != [] else []