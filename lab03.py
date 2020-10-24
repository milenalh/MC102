###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Bruto x Líquido
# Nome: Milena Lumi Hangai
# RA: 184654
###################################################

# Leitura de dados
b = float(input())


# Desconto de INSS
if b <= 1045:
    INSS = (b * 0.075)
if 1045.01 <= b <= 2089.6:
    INSS = (b * 0.09)
if 2089.61 <= b <= 3134.4:
    INSS = (b * 0.12)
if 3134.41 <= b <= 6101.06:
    INSS = (b * 0.14)
if b > 6101.06:
    INSS = (6101.06 * 0.14)


# Desconto de IR
y = (b - INSS)
if y <= 1903.98:
    IR = 0
if 1903.99 <= y <= 2826.65:
    IR = (y * 0.075) - 142.8
if 2826.66 <= y <= 3751.05:
    IR = (y * 0.15) - 354.8
if 3751.06 <= y <= 4664.68:
    IR = (y * 0.225) - 636.13
if y >= 4664.68:
    IR = (y * 0.275) - 869.36

# Saída de dados
salario_bruto = b
salario_liquido = y - IR
print("Bruto: R$", format(salario_bruto, ".2f").replace(".", ","))
print("INSS: R$", format(INSS, ".2f").replace(".", ","))
print("IR: R$", format(IR, ".2f").replace(".", ","))
print("Liquido: R$", format(salario_liquido, ".2f").replace(".", ","))