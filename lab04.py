###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Street Fighter
# Nome: Milena Lumi Hangai
# RA: 184654
###################################################


# Leitura do hp dos lutadores
hp_Ryu = int(input()) #vida do Ryu
hp_Ken = int(input()) #vida do Ken

# Leitura da sequência de golpes
gk = 0
gr = 0
while(hp_Ken > 0 and hp_Ryu > 0):
    x = int(input()) 
    if x > 0: 
        hp_Ken = (hp_Ken - x)
        gr = gr + 1
        print("RYU APLICOU UM GOLPE: %d" %x)
    if x < 0: 
        hp_Ryu = (hp_Ryu + x)
        gk = gk + 1
        print("KEN APLICOU UM GOLPE: %d" % abs(x))
    if (hp_Ken > 0 and hp_Ryu > 0):
        print("HP RYU = %d" %hp_Ryu)
        print("HP KEN = %d" %hp_Ken)
    elif (hp_Ken <= 0 and hp_Ryu > 0):
        print("HP RYU = %d" %hp_Ryu)
        print("HP KEN = 0")
    elif (hp_Ken > 0 and hp_Ryu <= 0):
        print("HP RYU = 0")
        print("HP KEN = %d" %hp_Ken)

# Impressão do vencedor e do número de golpes aplicados
if hp_Ryu <= 0:
    print("LUTADOR VENCEDOR: KEN")
if hp_Ken <= 0:
    print("LUTADOR VENCEDOR: RYU")
print("GOLPES RYU = %d" %gr)
print("GOLPES KEN = %d" %gk)