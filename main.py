from classes.banco import Banco
import os
from classes.usuario import Usuario

## TESTES

banco = Banco()
banco.abrirConexao()
banco.criarTabela()

## ENVIAR PARA O MENU
user = Usuario('Arthur', '123')
if banco.verificarDados(user):
    print('Usuario encontrado no banco!')
else:
    print('Usuario nao foi encontrado!')

banco.fecharConexao