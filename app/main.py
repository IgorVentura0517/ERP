
### Importando funções SQL dos arquivos models ###
from app.models_movimentacoes import criar_tabela_movimentacoes, inserir_movimentacao, listar_movimentacoes
from app.models_produtos import criar_tabela_produtos, inserir_produto, listar_produtos
from app.models_usuarios import criar_tabela_usuarios, inserir_usuario

### Chamada de funções para criação de tabelas ###
criar_tabela_produtos()
criar_tabela_usuarios()
criar_tabela_movimentacoes()



### Teste execução main.py ###
print("Executando.....")
