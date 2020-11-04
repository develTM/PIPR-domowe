
def b_kth(list):
    try:
        k = int(input("Podaj k: "))
        if k < len(list):
            return list[-k-1]
    except ValueError:
        print('input corrupt')
        return b_kth(list)

print(b_kth(range(20)))