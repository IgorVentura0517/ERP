from app.database import cursor, conexao

def criar_tabela_usuarios():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    """)
    conexao.commit()


def inserir_usuario(nome, tipo):
    cursor.execute("""
        INSERT INTO usuarios (nome, tipo)
        VALUES (?, ?)
    """, (nome, tipo))
    conexao.commit()