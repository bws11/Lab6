def sort_characters(string: str) -> str:
    # Sort for lower case
    # Then sort for upper case letters 

    # Transform into a list for easy sorting
    string = list(string)   

    changed: bool = True
    while changed:
        changed = False

        for i in range(1, len(string)):
            #lowercase sorting
            if string[i - 1].lower() > string[i].lower():
                string[i - 1], string[i] = string[i], string[i - 1]
                changed = True


    changed: bool = True
    while changed:
        changed = False

        for i in range(1, len(string)):
            # uppercase sorting ABOMINATION OF A IF STATEMENT
            if string[i - 1].lower() == string[i].lower() and string[i] == string[i].upper() and string[i] != string[i - 1]:
                string[i - 1], string[i] = string[i], string[i - 1]
                changed = True

    return ''.join(string)
