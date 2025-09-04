import string 

def anagrama(palavra1, palavra2):
    pass



def encontrar_maior_palavra(frase): #vai receber a grase como parâmetro
    palavras = frase.split() #cria uma lista da frase se baseando nos espaços
    maior_palavra = "" #vai guardar a maior palavra
    maior_tamanho = 0 #conta os caracteres da maior palavra 
    for palavra in palavras: #vai percorrer aquela transformação na linha 4
        palavra_limpa = palavra.strip(string.punctuation) #tira as pontuações
        if len(palavra_limpa) > maior_tamanho: #ve se a proxima palavra, já sem pontuação, é maior que a maior palavra guardada na variável maior_tamanho
            maior_palavra = palavra_limpa #se for maior, vai subtituir a maior palavra
            maior_tamanho = len(palavra_limpa) #atualiza o tamanho da maior palavra
    return maior_palavra 

print(encontrar_maior_palavra("O rato roeu a roupa do rei de Roma.")) #roupa com 5 letras
print(encontrar_maior_palavra("A jornada de mil milhas começa com um único passo.")) #jornada com 7 letras
print(encontrar_maior_palavra("Seja forte e corajoso")) #forte com 5 letras git 