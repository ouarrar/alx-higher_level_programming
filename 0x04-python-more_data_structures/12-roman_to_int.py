#!/usr/bin/python3
def subtract_list(listnum):
    sub = 0
    maxlist = max(listnum)

    for n in listnum:
        if maxlist > n:
            sub += n

    return (maxlist - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_num.keys())

    num = 0
    last = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_num.get(ch) <= last:
                    num += subtract_list(list_num)
                    list_num = [rom_num.get(ch)]
                else:
                    list_num.append(rom_num.get(ch))

                last = rom_num.get(ch)

    num += subtract_list(list_num)

    return (num)
