import classes.banco as Banco, classes.menu as Menu
import os

## TESTES
banco = Banco.Banco()
banco.criarTabela()
os.system('cls')

## MENU
menu = Menu.Menu()
opc = menu.telaInicial()

while opc != '0':
    if opc == '1':
        opc = menu.cConta()
    if opc == '2':
        opc = menu.lConta()
    if opc == '3':
        opc = menu.aConta()
    if opc == '4':
        opc = menu.dConta()
    if opc == '5':
        opc = menu.logar()
    if opc == '0':
        opc = menu.sair()

banco.fecharConexao