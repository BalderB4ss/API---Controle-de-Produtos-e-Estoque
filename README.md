# Controle de Produtos e Estoque

Aplicação simples para gerenciar um catálogo de produtos e o respectivo estoque. É composta por uma API (back-end) e uma interface em Streamlit (front-end).

## Funcionalidades
- Listar produtos (Catálogo)
- Adicionar produto (nome, categoria, preço, quantidade)
- Apagar produto por ID
- Atualizar preço de um produto
- Atualizar quantidade de um produto

## Estrutura esperada
- front-end/app.py — interface Streamlit (já presente)
- back-end/ (ou pasta equivalente) — API (ex.: FastAPI) que atende os endpoints descritos abaixo

> Observação: o front-end atual aponta para `API_URL = "http://127.0.0.1:8000"`. Ajuste se sua API rodar em outra porta/host.

## Endpoints usados pelo front-end
- GET /estoque
  - Retorna lista de produtos em JSON: { "produtos": [ { "id": ..., "nome": ..., "categoria": ..., "preco": ..., "quantidade": ... }, ... ] }
- POST /estoque
  - Parâmetros (query params): nome, categoria, preco, quantidade
  - Cria um produto
- DELETE /estoque/{id}
  - Remove produto por ID
- PUT /estoque/{id}
  - Parâmetro (query param): preco
  - Atualiza preço do produto
- PUT /estoque/quantidade/{id}
  - Parâmetro (query param): quantidade
  - Atualiza quantidade do produto

(O comportamento e respostas esperadas: status 200 em caso de sucesso; mensagens de erro em outros códigos)

## Requisitos
- Python 3.8+
- Pip

Dependências comuns sugeridas:
- fastapi
- uvicorn
- streamlit
- requests

Exemplo de arquivo requirements.txt:
```
fastapi
uvicorn
streamlit
requests
```

## Como executar (Windows)
1. Criar e ativar ambiente virtual (PowerShell)
   - python -m venv .venv
   - .\.venv\Scripts\Activate.ps1
2. Instalar dependências
   - pip install -r requirements.txt
3. Rodar a API (exemplo FastAPI)
   - cd back-end
   - uvicorn main:app --reload --port 8000
4. Rodar o front-end (a partir da raiz do projeto)
   - streamlit run front-end/app.py

Ajuste caminhos/nomes se sua API não estiver em `back-end` ou o módulo principal tiver outro nome.

## Observações e dicas
- Se o front não encontrar a API, verifique `API_URL` em `front-end/app.py`.
- Se usar FastAPI, habilite CORS se for acessar de domínios diferentes.
- Valide tipos/valores no back-end (preço >= 0, quantidade inteira >= 0).
- Para produção, não use `--reload` e rode com servidor ASGI adequado (ex.: gunicorn + uvicorn workers).

## Contribuição
- Abra uma issue descrevendo o problema ou a feature.
- Envie um pull request com mudanças pequenas e descrições claras.

## Licença
Balder - 2025.