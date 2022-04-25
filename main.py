import classes.banco as Banco, classes.menu as Menu, classes.usuario as Usuario
import os

## TESTES

banco = Banco.Banco()
banco.criarTabela()
os.system('cls')

## MENU
menu = Menu.Menu()
opc = menu.telaInicial()

if opc == '1':
    menu.cConta()

banco.fecharConexao