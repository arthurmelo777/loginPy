import classes.banco as Banco, classes.menu as Menu, classes.usuario as Usuario
import os

## TESTES

banco = Banco.Banco()
banco.excluirTabela()
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
    if opc == '0':
        opc = menu.sair()

banco.fecharConexao