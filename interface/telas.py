import PySimpleGUI as py

class Telas:
    def __init__(self):
        pass

    def janela_login(self):
        py.theme('Reddit')
        layout = [
            [py.Text('LOGIN')],
            [py.Text('Nome: ')],
            [py.Input(key='nome')],
            [py.Text('Senha: ')],
            [py.Input(key='senha')],
            [py.Button('Logar'), py.Button('Cadastrar-se')],
            [],
            [py.Text('', key='mensagem')]
        ]

        return py.Window('Login', layout= layout, finalize=True)
    
    def janela_cadastro(self):
        py.theme('Reddit')
        layout = [
            [py.Text('CADASTRO')],
            [py.Text('Nome: ')],
            [py.Input(key='nome')],
            [py.Text('Senha: ')],
            [py.Input(key='senha')],
            [py.Button('Cadastrar'), py.Button('Logar-se')],
            []
        ]

        return py.Window('Cadastro', layout=layout, finalize=True)
    
    def boas_vindas(self, nome):
        py.theme('Reddit')
        layout = [
            [py.Text('LOGIN BEM SUCEDIDO')],
            [py.Text(f'Bem vindo {nome}')],
            [py.Button('Excluir conta')],
            [py.Button('Sair')]
        ]

        return py.Window('Bem Vindo', layout=layout, finalize=True)