#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_len(tuple_a)
    tuple_b = check_len(tuple_b)
    retTupl = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    return retTupl


def check_len(tupl=()):
    if len(tupl) == 1:
        tupl = (tupl[0], 0)
    elif len(tupl) == 0:
        tupl = (0, 0)
    elif len(tupl) > 2:
        tupl = (tupl[0], tupl[1])
    return tupl
