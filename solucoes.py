palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()

def sao_anagramas(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    
    verificar1 = sorted(palavra1)
    verificar2 = sorted(palavra2)

    if verificar1 == verificar2:
        return True
    else:
        return False

def encontrar_maior_palavra(frase):
    pass

print(sao_anagramas(palavra1, palavra2))