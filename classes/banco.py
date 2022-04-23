import sqlite3, os

class Banco:
    def __init__(self): ## INICIAR O BANCO
        self.banco = sqlite3.connect('usuarios.db')
        self.cursor = sqlite3.Cursor(self.banco)
    
    def criarTabela(self): ## CRIAR TABELA
        self.cursor.execute("CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(15), senha VARCHAR(15))")
        self.banco.commit()
    
    def excluirTabela(self): ## EXCLUIR TABELA
        self.cursor.execute("DROP TABLE IF EXISTS User")
        self.banco.commit()

    def criarUsuario(self, usuario, senha): ## CRIAR USUARIO
        self.cursor.execute("INSERT INTO User VALUES (NULL, '"+usuario+"', '"+senha+"')")
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