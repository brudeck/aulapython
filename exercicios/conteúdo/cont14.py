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

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for c,v in enumerate(valores):
    print(f'na posição {c} eu achei o valor {v}', end='')