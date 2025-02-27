#FEITO POR: AUGUSTO VICTOR DA SILVA FERREIRA 
#turma:T2

import random
import os


def limpar_terminal():
    if os.name == "nt":  
        os.system("cls")
    else:  
        os.system("clear")


frutas = ["banana", "manga", "laranja", "melancia", "acerola"]
animais = ["cachorro", "gato", "calango", "cobra", "pombo"]
bairros = ["parangaba", "montese", "mondubim", "centro", "aldeota"]

partes_corpo = [ "perna direita", "perna esquerda", "braço direito",  "braço esquerdo", "tronco", "cabeça" ]


while True:
    print("escolha uma categoria: ")
    print("1 - frutas")
    print("2 - animais")
    print("3 - bairros")
    categoria = input("digite o numero da categoria: ")

    if categoria == "1":
            lista_palavras = frutas
    elif categoria == "2":
            lista_palavras = animais
    elif categoria == "3":
            lista_palavras = bairros
    else:
            print("Categoria inválida! Escolha novamente.")
            limpar_terminal()
            continue



    palavra_secreta = random.choice(lista_palavras)
    letras_acertadas = ["_"] * len(palavra_secreta)
    tentativas_maximas = 6
    tentativas_restantes = tentativas_maximas

    
    while tentativas_restantes > 0:
        
        print(" ".join(letras_acertadas))

       
        entrada = input("Digite uma letra ou a palavra completa: ").lower()

        
        if len(entrada) > 1:  
            if entrada == palavra_secreta:
                print("Você acertou a palavra e escapou da FORCA! Parabéns!")
                letras_acertadas = list(palavra_secreta) 
                break
            else:
                print(f"Você errou a palavra e foi para FORCA! A palavra secreta era: {palavra_secreta}")
            tentativas_restantes = 0  
            break 

        
        else:
            letra = entrada
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_acertadas[i] = letra

            
            if letra not in palavra_secreta:
                tentativas_restantes -= 1
                parte = partes_corpo[6 - tentativas_restantes - 1] 
                print(f"Você errou! Sua {parte} está na forca. Tentativas restantes: {tentativas_restantes}")

        
        if "_" not in letras_acertadas:
            print("Parabéns! Você acertou a palavra secreta e escapou da FORCA!")
            break

        
        if tentativas_restantes == 0:
            print(f"Você perdeu e você foi ENFORCADO. A palavra secreta era: {palavra_secreta}")
            break
    
    
    
    jogar_novamente = input("Quer tentar a sorte novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        break

    limpar_terminal()