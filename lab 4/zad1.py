
def b_kth(list):
    try:
        k = int(input("Podaj k: "))
        if 0 < k <= len(list):
            return list[-k]
        print('value out of range')
        return b_kth(list)
    except ValueError:
        print('input corrupt')
        return b_kth(list)

print(b_kth(range(20)))