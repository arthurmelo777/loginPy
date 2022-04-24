import sqlite3, os

class Banco:
    def __init__(self):
        pass

    def abrirConexao(self): ## INICIAR O BANCO
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

    def lerUsuario(self, id): ## LER USUARIO
        self.cursor.execute("SELECT * FROM User WHERE id = "+id+"")
        r = self.cursor.fetchall()

        return r[0]
    
    def atualizarUsuario(self, id, b, valor): ## ATUALIZAR USUARIO
        if b == 'U':
            self.cursor.execute("UPDATE User SET nome = '"+valor+"' WHERE id = "+id+"")
        elif b == 'S':
            self.cursor.execute("UPDATE User SET senha = '"+valor+"' WHERE id = "+id+"")
        self.banco.commit()
    
    def deletarUsuario(self, id): ## DELETAR USUARIO
        self.cursor.execute("DELETE FROM User WHERE id = "+id+"")
        self.banco.commit()
    
    ## VERIFICAR SE HÁ DADOS COMPATIVEIS NO BANCO

    def verificarDados(self, usuario):
        self.cursor.execute("SELECT * FROM User")
        r = self.cursor.fetchall()

        for v in r:
            if v[1] == usuario.user and v[2] == usuario.password:
                return True
            break
