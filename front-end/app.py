import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

response = requests.get(f"{API_URL}/estoque")
if response.status_code == 200:
    produtos = response.json().get("produtos", [])
    ids = [linha["id"] for linha in produtos]

st.set_page_config(page_title="Controle de Produtos e Estoque", page_icon="🚚")
st.title("🚛 Controle de Produtos e Estoque")
menu = st.sidebar.radio("Navegação", ["Catálogo","Adicionar Produto","Apagar Produto","Atualizar Produto"])
if menu =="Catálogo":
    st.subheader("Todos os produtos disponíveis")
    response = requests.get(f"{API_URL}/estoque")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            tabela_estoque = {
                "ID": [produto['id'] for produto in produtos],
                "Nome": [produto['nome'] for produto in produtos],
                "Categoria": [produto['categoria'] for produto in produtos],
                "Preço/unidade": [f"{produto['preco']:,.2f}" for produto in produtos],
                "Quantidade": [produto['quantidade'] for produto in produtos],
            }
            st.table(tabela_estoque)
        else:
            st.warning("Não há nenhum produto cadastrado!")
    else:
        st.error("Erro ao acessar a API❗")
        
elif menu == "Adicionar Produto":
    st.subheader("➕ Adicionar Produto ➕")
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("Categoria do produto")
    preco = st.number_input("Preço/unidade", min_value=0.01, step=0.5)
    quantidade = st.number_input("Quantidade)", min_value=1, step=1)
    if st.button("Adicionar"):
        dados = {"nome": nome, "categoria": categoria, "preco":preco, "quantidade":quantidade}
        response = requests.post(f"{API_URL}/estoque", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o produto❗")

elif menu == "Apagar Produto":
    st.subheader("❌ Apagar Produto ❌")
    if ids:
        escolha = st.selectbox("Escolha o ID do produto para apagar",ids)
        response = requests.get(f"{API_URL}/estoque")
        if response.status_code == 200:
            produtos = response.json().get("produtos",[])
            produto_selecionado = next((linha for linha in produtos if linha["id"] == escolha), None)
            if produto_selecionado:
                st.dataframe([produto_selecionado])
            else:
                st.error("Erro ao buscar detalhes do produto")
        if st.button("⚠Deletar⚠"):
            response = requests.delete(f"{API_URL}/estoque/{escolha}")
            if response.status_code == 200:
                st.success("Sucesso ao apagar produto!")
            else:
                st.error("Erro ao deletar produto❗")
    else:
        st.info("Nenhum produto disponível para deletar!")

elif menu == "Atualizar Produto":
    aba1, aba2 = st.tabs(["Preço", "Quantidade"])
    with aba1:
        st.subheader("📦 Atualizar Preço do Produto 📦")
        if not ids:
            st.warning("Nenhum produto disponível para atualizar")
        else:
            escolha = st.selectbox("Selecione o ID do produto para atualizar",ids, key="select_preco")
            response = requests.get(f"{API_URL}/estoque")
            if response.status_code == 200:
                produtos = response.json().get("produtos", [])
                produto_selecionado = next((item for item in produtos if item["id"] == escolha), None)
                if produto_selecionado:
                    st.dataframe([produto_selecionado])
                else:
                    st.error("Erro ao buscar detalhes do produto")
                preco = st.number_input("Novo preço", value=0.01, format="%.2f", key="input_preco")
                if st.button("Atualizar Produto ✔", key="btn_preco"):
                    dados = {
                        "preco": preco,
                    }
                    response = requests.put(f"{API_URL}/estoque/{escolha}", params=dados)
                    if response.status_code == 200:
                        st.success("Produto atualizado com sucesso!")
                    else:
                        st.error("Erro ao atualizar produto❗")
    with aba2:
        st.subheader("📦 Atualizar Quantidade do Produto 📦")
        if not ids:
            st.warning("Nenhum produto disponível para atualizar")
        else:
            escolha = st.selectbox("Selecione o ID do produto para atualizar",ids, key="select_qtd")
            response = requests.get(f"{API_URL}/estoque")
            if response.status_code == 200:
                produtos = response.json().get("produtos", [])
                produto_selecionado = next((item for item in produtos if item["id"] == escolha), None)
                if produto_selecionado:
                    st.dataframe([produto_selecionado])
                else:
                    st.error("Erro ao buscar detalhes do produto")
                quantidade = st.number_input("Nova quantidade", value=1, key="input_qtd")
                if st.button("Atualizar Produto ✅",key="btn_qtd"):
                    dados = {
                        "quantidade": quantidade,
                    }
                    response = requests.put(f"{API_URL}/estoque/quantidade/{escolha}", params=dados)
                    if response.status_code == 200:
                        st.success("Produto atualizado com sucesso!")
                    else:
                        st.error("Erro ao atualizar produto❗")