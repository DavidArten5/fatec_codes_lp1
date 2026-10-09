# Seu código aqui
valor_venal= float(input("qual o valor venal?: R$"))

if valor_venal<= 100000.00:
    print("isento")
elif valor_venal <= 250000.00:
    iptu = valor_venal * 0.005 - 500
    iptu= str(iptu)
    print("vc pagara " + iptu + " de IPTU")
elif  valor_venal <= 500000.00:
    iptu = valor_venal * 0.01 - 1750
    iptu= str(iptu)
    print("vc pagara " + iptu + " de IPTU")
elif valor_venal <= 1000000.00:
    iptu = valor_venal * 0.015 - 4250
    iptu= str(iptu)
    print("vc pagara " + iptu + " de IPTU")
else :
    iptu = valor_venal * 0.02 - 9250
    iptu= str(iptu)
    print("vc pagara " + iptu + " de IPTU")