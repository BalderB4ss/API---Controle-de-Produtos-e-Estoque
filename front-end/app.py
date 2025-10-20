import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Controle de Produtos e Estoque", page_icon="🚚")
st.title("🚛 Controle de Produtos e Estoque")

menu = st.sidebar.radio("Navegação", ["Catálogo","Adicionar Produto","Apagar Produto","Atualizar Produto"])
if menu =="Catálogo":
    st.subheader("Todos os produtos disponíveis")
    response = requests.get(f"{API_URL}/estoque")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            tabela_produtos = {
                "ID": [produto['id'] for produto in produtos],
                "Nome": [produto['nome'] for produto in produtos],
                "Categoria": [produto['categoria'] for produto in produtos],
                "Preço/unidade": [f"{produto['preco']:,.2f}" for produto in produtos],
                "Quantidade": [produto['quantidade'] for produto in produtos],
            }
            st.table(tabela_produtos)
        else:
            st.warning("Não há nenhum produto cadastrado!")
    else:
        st.error("Erro ao acessar a API❗")