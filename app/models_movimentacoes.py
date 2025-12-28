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

def inserir_movimentacao(
    produto_id,
    usuario_id,
    tipo,
    quantidade,
    descricao=None
):
    cursor.execute("""
        INSERT INTO movimentacoes
        (produto_id, usuario_id, tipo, quantidade, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (produto_id, usuario_id, tipo, quantidade, descricao))

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


def listar_movimentacoes():
    cursor.execute("""
        SELECT 
            m.id,
            p.nome,
            m.tipo,
            m.quantidade,
            m.descricao,
            m.data
        FROM movimentacoes m
        JOIN produtos p ON p.id = m.produto_id
        ORDER BY m.data DESC
    """)
    return cursor.fetchall()