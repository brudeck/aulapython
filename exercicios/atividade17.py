km=float(input('quantos km foram percorridos?'))
dia=int(input('quantos km foram percorridos?'))
precodias = dia*60
precokm = km*0.15
total = precodias + precokm
print('total a pagar pelo aluguel é: R${:.2f}'.format(total))