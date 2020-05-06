#!/usr/bin/env python


def find_max(str_rep: str):
    char_to_replace = None
    for char in str_rep:
        if char != "9":
            # replace all values 
            char_to_replace = char
            break
    new_str = []
    if char_to_replace is not None:
        for char in str_rep:
            if char == char_to_replace:
                new_str.append("9")
            else:
                new_str.append(char)
        return int("".join(new_str))
    else:
        return int(str_rep)


def find_min(str_rep: str):
    char_to_replace = None
    replace_to = None
    is_first_char_one = False

    # also can't replace to zero if the first char is 1
    for ix, char in enumerate(str_rep):
        if ix == 0 and char == "1":
            is_first_char_one = True

        if char != "0" and ix > 0:
            if not is_first_char_one:
                char_to_replace = char
                replace_to = "0"
                break
            else:
                if char != "1":
                    char_to_replace = char
                    replace_to = "0"
                    break
        elif ix == 0 and char != "1":
            char_to_replace = char
            replace_to = "1"
            break

    new_str = []

    if char_to_replace is not None:
        for char in str_rep:
            if char == char_to_replace:
                new_str.append(replace_to)
            else:
                new_str.append(char)
        return int("".join(new_str))
    else:
        return int(str_rep)



def main(num: int):
    str_rep = str(num)

    _max = find_max(str_rep)
    _min = find_min(str_rep)

    return _max - _min



if __name__ == '__main__':
    print(main(1101057))
    # expected: 8808050
