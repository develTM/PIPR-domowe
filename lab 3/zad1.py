
def merge_segments(x, y):
    if x[0] < y[0]: #wskaż odcinek po lewej
        if x[1] < y[0]: return None
        return y[0], min(x[1], y[1])
    if y[1] < x[0]: return None
    return x[0], min(x[1], y[1])

print(merge_segments((3,4),(1, 6)))

