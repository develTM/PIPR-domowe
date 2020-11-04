
def full_row(width):
    print(width *'*')

def two_dot_row(width):
    for i in range(width):
        if i==0 or i==width-1: print('*', end='')
        else: print(' ', end='')
    print('')

def middle_row(what, width):
    #ustawia słowo na środu albo 1 komórkę w lewo jak się nie da
    space = int(0.5 * (width - 2 - len(what)))
    print('*', end='')
    for i in range(space): print(' ', end='')
    print(what,end='')
    for i in range(space): print(' ', end='')
    if ((width + len(what)) % 2 == 0):
        print('*')
    else:
        print(' *')

def highlight(what, width):
    print('')
    full_row(width)
    two_dot_row(width)
    middle_row(what, width)
    two_dot_row(width)
    full_row(width)

#highlight('TV TRFAM', 20)

def fun(p1,p2):
    print('{:*>{size}}'.format("",size=p2))
    print('*'+':{size}}'.format("",size=p2-2)+'*')
    print('*'+'{:^{size}}'.format(p1,size=p2-2)+'*')
    print('*'+'{:{size}}'.format("",size=p2-2)+'*')
    print('{:*>{size}}'.format("",size=p2))

#fun("Hello",12)


print('{:*<{size}}'.format('slowo',size=10))