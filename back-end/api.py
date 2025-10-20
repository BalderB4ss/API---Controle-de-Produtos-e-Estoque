from fastapi import FastAPI
from funcao import adicionar_produto, atualizar_preco, atualizar_quantidade, excluir_produto, listar_todos

app = FastAPI(title="Controle de Produtos e Estoque")

@app.get("/")
def home():
    return {"mensagem": "Api de Controle de Produtos e Estoque"}

@app.post("/produtos")
def criar_produto(nome:str, categoria:str, preco:float, quantidade:int):
    adicionar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "produto adicionado com sucesso!"}
