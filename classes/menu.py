import os
from classes.banco import Banco
from classes.usuario import Usuario

class Menu:
    def __init__(self):
        self.bd = Banco()

    ## MOSTRA TELA INICIAL DO MENU

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
    
    ## CRIAR CONTA

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
        self.opc = self.telaInicial()

        return self.opc
    
    ## LER DADOS DE UMA CONTA

    def lConta(self):
        while True:
            print('Digite o ID da conta que deseja consultar: ')
            v = input()
            os.system('cls')
            u = self.bd.lerUsuario(v)
            os.system('cls')

            if u:
                print(f"""
ID: {u[0]}
Username: {u[1]}
Senha: {u[2]}
                    """)
                input('Aperte qqr tecla para continuar.')
                break
        os.system('cls')
        self.opc = self.telaInicial()

        return self.opc

    ## ATUALIZAR DADOS DA CONTA

    def aConta(self):
        while True:
            print("""
DIgite respectivamente o ID da conta, o campo e o valor que deseja atualizar:
    Exemplo: ID campo valor""")
            v= input().split()
            os.system('cls')
            u = self.bd.atualizarUsuario(v[0], v[1], v[2])
            os.system('cls')

            if u:
                input("Valor atualizado! Aperte qqr tecla para continuar.")
                break
        os.system('cls')
        self.opc = self.telaInicial()

        return self.opc
    
    ## DELETAR CONTA

    def dConta(self):
        while True:
            print('Digite o ID da conta que deseja excluir: ')
            v = input()
            os.system('cls')
            u = self.bd.deletarUsuario(v)
            os.system('cls')

            if u:
                input("Conta excluída com sucesso! Aperte qqr tecla para continuar.")
                break
        os.system('cls')
        self.opc = self.telaInicial()

        return self.opc
    
    ## LOGAR

    def logar(self):
        while True:
            print("""
Digite respectivamente o login e a senha da conta que deseja entrar:
    Exemplo: login senha""")
            v = input().split()
            os.system('cls')
            
            if self.bd.verificarDados(Usuario(v[0], v[1])):
                input(f"""
Logado com sucesso! Bem vindo {v[0]}!
Aperte qqr tecla para continuar""")
                break
            else:
                input("""
Login incorreto, por favor tente novamente!
Aperte qqr tecla para continuar""")
                os.system('cls')
        os.system('cls')
        self.opc = self.telaInicial()

        return self.opc
    
    ## SAIR DO MENU

    def sair(self):
        input('Obrigado por usar nosso programa, até logo!')
        os.system('cls')
