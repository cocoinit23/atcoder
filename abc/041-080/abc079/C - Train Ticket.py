n = [int(x) for x in input()]

op_num = len(n) - 1

for i in range(2 ** op_num):
    op = ['+'] * op_num
    for j in range(op_num):
        if (i >> j) & 1:
            op[op_num - 1 - j] = '-'

    op.append('')
    formula = ''
    for x, o in zip(n, op):
        formula += str(x) + o
    if eval(formula) == 7:
        print(formula + '=7')
        break
