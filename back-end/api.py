from fastapi import FastAPI
from funcao import adicionar_produto, atualizar_preco, atualizar_quantidade, excluir_produto, listar_todos, buscar_produto

app = FastAPI(title="Controle de Produtos e Estoque")

@app.get("/")
def home():
    return {"mensagem": "Api de Controle de Produtos e Estoque"}

@app.post("/estoque")
def criar_produto(nome:str, categoria:str, preco:float, quantidade:int):
    adicionar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "produto adicionado com sucesso!"}

@app.get("/estoque")
def exibir_todos():
    produtos = listar_todos()
    lista = []
    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome": produto[1],
            "categoria": produto[2],
            "preco": produto[3],
            "quantidade":produto[4]})
    return {"produtos": lista}

@app.delete("/estoque")
def apagar_produto(id:int):
    excluir_produto(id)
    return {"Mensagem": "Produto deletado com sucesso!"}

@app.put("/estoque/preco")
def att_preco(id:int,preco:float):
    produto = buscar_produto(id)
    if produto:
        atualizar_preco(id, preco)
        return {"mensagem": "Produto atualizado com sucesso!"}
    return {"erro": "Produto não encontrado!"}