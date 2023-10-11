#!/usr/bin/python3
def subtract_list(listnum):
    tosub = 0
    maxlist = max(listnum)

    for n in listnum:
        if maxlist > n:
            tosub += n

    return (maxlist - tosub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_num.keys())

    num = 0
    lastnum = 0
    listnum = [0]

    for c in roman_string:
        for k in list_keys:
            if k == c:
                if roman_num.get(c) <= lastnum:
                    num += subtract_list(listnum)
                    listnum = [roman_num.get(c)]
                else:
                    listnum.append(roman_num.get(c))

                lastnum = roman_num.get(c)

    num += subtract_list(listnum)

    return (num)

