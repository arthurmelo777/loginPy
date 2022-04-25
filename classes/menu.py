import os
from classes.banco import Banco
from classes.usuario import Usuario

class Menu:
    def __init__(self):
        self.bd = Banco()

    def telaInicial(self):
        print("""
Bem vindo ao sistema de login, escolha uma opção abaixo: 
    1 - Criar conta
    2 - Verificar dados da conta
    3 - Atualizar dados da conta
    4 - Excluir conta
    5 - Logar
    0 - Sair"""
    )
        self.opc = input()
        os.system('cls')

        return self.opc
    
    def cConta(self):
        while True:
            print("""
Para criar sua conta digite, respectivamente, o seu nome de usuario e sua senha
    Exemplo: usuario senha""")
            v = input().split()
            b = self.bd.criarUsuario(Usuario(v[0], v[1]))

            if self.bd.verificarDados(Usuario(v[0], v[1])) and b:
                print('Usuario cadastrado com sucesso!')
                input('Aperte qualquer tecla para continuar')
                break
            os.system('cls')