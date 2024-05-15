from time import sleep
from random import choice, random, choices, randint, random

caverna = ["Larvitar","Aron","Rockruff","Swinub","Diglett","Rhyhorn","Meltan","Skarmory","Steelix","Meowth"]
matagal = ["Caterpie","Pinsir","Wurmple","Paras","Chikorita","Bulbasaur","Hoppip","Pidgey","Zubat","Mantine"]
primeiro_pokemon = []
pokedex = []
pokebolas = 3
chance = 0.3
def linha():
    print("=" * 70)


def introducao():
    print("=" * 70)
    print("POKÉMON WORLD".center(70))
    print("=" * 70)
    print("Carvalho: Olá, bem vindo ao pokémon world,")
    print("          eu serei seu professor, meu nome")
    print("          é Carvalho e o seu nome qual é? ")
    nome = str(input("          >>>"))
    sleep(0.5)
    print(f"Carvalho: Muito prazer {nome},")
    print("          vamos para a aventura!\n")


def pokemons_iniciais():
    while True:
        pokeinicial = str(input("Escolha um pokémon para iniciar: \n [1] Charmander \n [2] Pikachu \n [3] Rattata \n >>>"))
        if pokeinicial in "123":
            if pokeinicial == "1":
                primeiro_pokemon.append("Charmander")
                pokedex.append("Charmander")
                print("Ótima escolha! Charmander é um ótimo pokémon do tipo fogo.")
            elif pokeinicial == "2":
                primeiro_pokemon.append("Pikachu")
                pokedex.append("Pikachu")
                print("Ótima escolha! Pikachu é um ótimo pokémon do tipo elétrico.")
            elif pokeinicial == "3":
                primeiro_pokemon.append("Rattata")
                pokedex.append("Rattata")
                print("Ótima escolha! Rattata é um ótimo pokémon do tipo normal.")
            break
        else:
            print("Comando inválido! Tente novamente.")
            continue


def escolha():
    print("Oque você deseja fazer?")
    linha()
    while True:
        escolha = str(input(" [1] Entrar na caverna\n [2] Entrar no matagal\n [3] Listar Pokémon da Pokédex\n [4] Sair\n >>> "))
        if escolha not in "1234":
            continue
        else:
            break
    return escolha

def quantpokebolas():
    global pokebolas
    linha()    
    print(f"Você possui:{pokebolas} pokebolas")
    if random() < chance:
        quant_pokebolas = randint(1, 2)
        pokebolas += quant_pokebolas
        print(f"Você conseguiu {quant_pokebolas} pokebolas, agora está com {pokebolas}")
    else:
        linha()
        print("Nenhuma pokebola adquirida desta vez")
        linha()

def sorteio(lista_pokemons):
    return choice(lista_pokemons)

def menu():
    introducao()
    linha()
    pokemons_iniciais()
    linha()
    while True:
        pokebolas = 3
        probabilidade = []
        acao = escolha()
        captura = [1,2]
        encontrado = ''  
        if acao == "1":
            print("Boa escolha, o ambiente o Caverna é ótimo para pokémons do tipo pedra, terra e aço.")
            encontrado = sorteio(caverna)
            sleep(1)
            print(f"Você entrou na caverna e encontrou um {encontrado}!")
            probabilidade = [50,50]
        elif acao == "2":
            print("Boa escolha, o ambiente Matagal é ótimo para pokémons do tipo inseto, planta e voador.")
            encontrado = sorteio(matagal)
            sleep(1)
            print(f"Você entrou no matagal e encontrou um {encontrado}!")
            probabilidade = [35,65]
        elif acao == "3":
            print("="*70)
            print(f"Lista de pokémons na sua pokedex: {pokedex}\nQuantidade de pokebolas: {pokebolas}")
            print("="*70)
            continue
        elif acao == "4":
            print("Até mais aventureiro!")
            linha()
            break
        quantpokebolas()
        if pokebolas == 0:
            print("Acabou suas pokebolas!")
            print("Fim de jogo!")
        if encontrado in pokedex:
            print("Este pokémon já está no seu pokedex, não haverá processo de captura!")
            sleep(1)
            break
        else:
            cont = 0
            while True:
                resp = str(input("Deseja capturar este pokémon? [S/N]:"))
                if resp.lower() != "s" and resp.lower() != "n":
                    print("Comando desconhecido! Informe novamente.")
                elif resp == "s":
                    cont += 1
                    num = choice(choices(captura, probabilidade, k=100))
                    if num == 1:
                        print(f"Você capturou um {encontrado}!")
                        pokedex.append(encontrado)
                        sleep(1)
                        break
                    elif num == 2:
                        if cont != 3:
                            pokebolas -= 1
                            print("Você não conseguiu captura-lo!")
                            print("Você perdeu 1 pokebola!")
                            continue
                        if cont == 3:
                            pokebolas -= 1
                            print("O pokémon fugiu!")
                            print("Você perdeu 1 pokebola!")
                            sleep(1)
                            break
                elif resp == "n":
                    break


menu()