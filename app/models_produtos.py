from app.database import cursor, conexao

def criar_tabela_produtos():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            nome TEXT NOT NULL,
            preco_custo REAL NOT NULL,
            preco_venda REAL NOT NULL,
            categoria TEXT,
            quantidade INTEGER NOT NULL
        )
    """)
    conexao.commit()

def inserir_produto(codigo, nome, preco_custo, preco_venda, categoria, quantidade):
    cursor.execute("""
        INSERT INTO produtos 
        (codigo, nome, preco_custo, preco_venda, categoria, quantidade)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (codigo, nome, preco_custo, preco_venda, categoria, quantidade))
    conexao.commit()



def listar_produtos():
    cursor.execute("""SELECT * FROM produtos""")
    return cursor.fetchall()