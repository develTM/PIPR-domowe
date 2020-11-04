
def criss_cross(data):
    for i in range(3):
        if data[i][0] == data[i][1] == data[i][2]:
            return data[i][0]
        elif data[0][i] == data[1][i] == data[2][i]:
            return data[0][i]
    if data[0][0] == data[1][1] == data[2][2] or data[0][2] == data[1][1] == data[2][0] :
        return data[1][1]
    return None

data = [['o', 'x', 'o'],
        ['x', 'o', 'o'],
        ['x', 'o', 'x']]
print(criss_cross(data))