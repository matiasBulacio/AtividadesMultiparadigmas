# from itens import arma, armadura, pocao
# print(arma.Arma("Espada").usar())
# from itens import *
from itens import Pocao, Arma, Armadura

def main():
    faca = Arma("Tramontina")
    faca.usar()

    pocao = Pocao("Suco")
    pocao.usar()

    armadura = Armadura("roupa de pano")
    armadura.usar()

if __name__ == "__main__":
    main()