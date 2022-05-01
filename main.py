from asyncio.windows_events import NULL
import classes.banco as Banco, classes.usuario as Usuario, interface.telas as Telas
import PySimpleGUI as py

## TESTES
banco = Banco.Banco()
banco.criarTabela()
tela = Telas.Telas()
user = Usuario.Usuario
logado = NULL

login, cadastro, bemVindo = tela.janela_login(), None, None

while True:
    window, event, values = py.read_all_windows()

    ## FECHAR JANELA

    ## JANELA LOGIN
    if window == login and event == py.WIN_CLOSED:
        break
    elif window == login and event == 'Logar':
        nome, senha = values['nome'], values['senha']
        if banco.logar(user(nome, senha)):
            logado = user(nome, senha)
            bemVindo = tela.boas_vindas(nome)
            login.hide()
    elif window == login and event == 'Cadastrar-se':
        cadastro = tela.janela_cadastro()
        login.hide()
    ## JANELA CADASTRO
    elif window == cadastro and event == py.WIN_CLOSED:
        break
    elif window == cadastro and event == 'Cadastrar':
        nome, senha = values['nome'], values['senha']
        if banco.logar(user(nome, senha)) == False:
            banco.criarUsuario(user(nome, senha))
            cadastro.hide()
            login = tela.janela_login()
    elif window == cadastro and event == 'Logar-se':
        cadastro.hide()
        login = tela.janela_login()
    ## JANELA BOAS VINDAS
    elif window == bemVindo and event == py.WIN_CLOSED:
        break
    elif window == bemVindo and event == 'Excluir conta':
        if banco.logar(logado):
            banco.excluirUsuario(user(nome, senha))
            bemVindo.hide()
            login = tela.janela_login()
    elif window == bemVindo and event == 'Sair':
        logado = NULL
        bemVindo.hide()
        login = tela.janela_login()

banco.fecharConexao()