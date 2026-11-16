def counter(max: int, start: int):
    start -= 1
    outputted = []

    while start < max:
        start += 1
        print(start)
        outputted.append(start)
        
    return outputted