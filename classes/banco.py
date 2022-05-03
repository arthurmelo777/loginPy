import sqlite3, os

class Banco:
    def __init__(self): ## INICIAR O BANCO
        self.banco = sqlite3.connect('usuarios.db')
        self.cursor = sqlite3.Cursor(self.banco)
    
    def fecharConexao(self): ## FECHAR O BANCO
        self.banco.close()
    
    def criarTabela(self): ## CRIAR TABELA
        self.cursor.execute("CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(15), senha VARCHAR(15))")
        self.banco.commit()
    
    def excluirTabela(self): ## EXCLUIR TABELA
        self.cursor.execute("DROP TABLE IF EXISTS User")
        self.banco.commit()

    def criarUsuario(self, usuario): ## CRIAR USUARIO
        self.cursor.execute("INSERT INTO User VALUES (NULL, '"+usuario.user+"', '"+usuario.password+"')")
        self.banco.commit()

    def excluirUsuario(self, usuario): ## EXCLUIR USUARIO
        self.cursor.execute("DELETE FROM User WHERE nome = '"+usuario.user+"' AND senha = '"+usuario.password+"'")
        self.banco.commit()
    
    def logar(self, usuario): ## LOGAR
        if self.verificarDados(usuario): return True
        else: return False
    
    ## VERIFICAR SE HÁ DADOS COMPATIVEIS NO BANCO

    def verificarDados(self, usuario):
        self.cursor.execute("SELECT * FROM User")
        r = self.cursor.fetchall()

        for v in r:
            if (str(v[1]).upper() == str(usuario.user).upper() and v[2] == usuario.password) or v[1] == usuario.user:
                return True