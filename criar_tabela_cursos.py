import sqlite3
conexao = sqlite3.connect('sqlite.git')
cursor = conexao.cursor()


sql = '''
CREATE TABLE cursos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT (100),
    descrição TEXT(100),
    data TEXT (8)
);
'''
cursor.execute(sql)
print('\033[1;32mDADOS INSERIDOS COM SUCESSO!')
conexao.commit()
conexao.close()

