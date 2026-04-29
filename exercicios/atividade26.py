velocidade = float(input("Qual a velocidade do carro em km/h? "))
limite = 80
if velocidade > limite:
    km_excedidos = velocidade - limite
    multa = km_excedidos * 7
    print("MULTADO! Você excedeu o limite de {}km/h.".format(limite))
    print("Velocidade registrada: {}km/h".format(velocidade))
    print("Valor da multa: R${:.2f}".format(multa))
else:
    print("Velocidade dentro do limite. Dirija com segurança!")