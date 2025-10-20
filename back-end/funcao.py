from conexao import conectar
def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
categoria VARCHAR(50),
preco NUMERIC(10,2),
quantidade INT
)
""")
            conexao.commit()
        except Exception as error:
            print(f"Erro ao criar tabela: {error}")
        finally:
            cursor.close()
            conexao.close()

def adicionar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                           (nome, categoria, preco, quantidade))
            conexao.commit()
        except Exception as error:
            print(f"Erro ao inserir filme: {error}")
        finally:
            cursor.close()
            conexao.close()
