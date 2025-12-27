from app.database import cursor, conexao

def criar_tabela_movimentacoes():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            descricao TEXT,
            data DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (produto_id) REFERENCES produtos(id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    """)
    conexao.commit()

def inserir_movimentacao(produto_id, usuario_id, tipo, quantidade, descricao):
    # registra movimentação
    cursor.execute("""
        INSERT INTO movimentacoes 
        (produto_id, usuario_id, tipo, quantidade, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (produto_id, usuario_id, tipo, quantidade, descricao))

    # atualiza estoque
    if tipo == "entrada":
        cursor.execute("""
            UPDATE produtos
            SET quantidade = quantidade + ?
            WHERE id = ?
        """, (quantidade, produto_id))

    elif tipo == "saida":
        cursor.execute("""
            UPDATE produtos
            SET quantidade = quantidade - ?
            WHERE id = ?
        """, (quantidade, produto_id))

    conexao.commit()