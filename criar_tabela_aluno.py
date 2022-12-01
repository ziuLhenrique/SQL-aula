import sqlite3
conexao = sqlite3.connect('sqlite.git')
cursor = conexao.cursor()

sql = '''
CREATE TABLE aluno (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email TEXT (100) NOT NULL,
    senha TEXT (50) NOT NULL,
    nome TEXT (100) NOT NULL,
    CONSTRAINT aluno_UN UNIQUE (email)
);
'''

cursor.execute(sql)
print('\033[1;32mDados inseridos com sucesso!')
conexao.commit()
conexao.close()