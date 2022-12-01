import sqlite3
conexao = sqlite3.connect('sqlite.git')
cursor = conexao.cursor()

sql = '''
CREATE TABLE inscricao(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    curso_id INTEGER NOT NULL,
    aluno_id INTEGER NOT NULL,
    data TEXT (8),
    CONSTRAINT inscricao_FK FOREIGN KEY (curso_id) REFERENCES curso(id),
    CONSTRAINT inscricao_FK_1 FOREIGN KEY (aluno_id) REFERENCES aluno(id)
);
'''
cursor.execute(sql)
print('\033[4;32mDADOS INSERIDOS COM SUCESSO!')
conexao.commit()
conexao.close()