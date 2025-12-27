from app.models_movimentacoes import criar_tabela_movimentacoes, inserir_movimentacao
from app.models_produtos import criar_tabela_produtos, inserir_produto
from app.models_usuarios import criar_tabela_usuarios, inserir_usuario

criar_tabela_produtos()
criar_tabela_usuarios()
criar_tabela_movimentacoes()


print("Executando.....")