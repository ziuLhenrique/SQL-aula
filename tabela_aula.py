import sqlite3
conexao = sqlite3.connect('sqlite.git')
cursor = conexao.cursor()


sql = '''
CREATE TABLE aula(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    curso_id INTEGER NOT NULL,
    nome TEXT (100) NOT NULL,
    ordem INTEGER NOT NULL,
    conteudo TEXT,
    CONSTRAINT aula_FK FOREIGN KEY (curso_id) REFERENCES curso(id)
);
'''
cursor.execute(sql)
print('\033[1;32mDADOS INSERIDOS COM SUCESSO!')
conexao.commit()
conexao.close()