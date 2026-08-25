# num = [2,5,9,1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2,2)
# num.remove(2)

# if 4 in num:
#     num.remove(4)
# else:
#     print('não achei o número 4')
# num.pop(2)
# print(num)

#[] significa lista
#() significa tuplas

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
# print(valores)
# for c,v in enumerate(valores):
#     print(f'na posição {c} eu achei o valor {v}', end='')

# valores = []
# for cont in range(0,5):
#     valores . append(int(input('digite um valor')))
# for c,v in enumerate(valores):
#     print(f'eu achei na posição {c} o valor de {v}')

a = [2,3,4,7]
b = [4,5,6,7]
#b = a
b = a[:]
b [2] = 8
print(f'lista a {a}')
print(f'lista b {b}')
