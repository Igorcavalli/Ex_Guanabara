print("{:=^50}".format(" LOJAS CAVALLI "))

compra = float(input("Informe o Valor da compra: R$ "))

print(""" FORMAS DE PAGAMENTO:

[1] A vista cheque/cartao.
[2] A vista cartao.
[3] 2x cartao de credito.
[4] 3x Cartao de credito (com juros)
""")

pagamento = int(input("Qual a opcao de pagamento? "))

if pagamento == 1:
    print(f"O valor da sua compra com desconto e: R$ {compra -(compra *10/100):.2f} reais")
elif pagamento == 2:
    print(f"O valor da sua compra e: R$ {compra - (compra*5/100):.2f} reais")
elif pagamento == 3:
    print(f"Sua compra e de: R$ {compra}, dividido em duas parcelas de R$ {compra/2:.2f} reais.")
elif pagamento == 4:
    print(f"Sua compra e de: R$ {compra}, dividido em tres parcelas de R$ {(compra*1.2)/3:.2f} reais.")
