


# Api de Doação de Livros VnW



## 🚀 Como Executar o Projeto

### 1️⃣ Visualizar o Código no GitHub
- Navegue pelos arquivos na estrutura do projeto para ver o código Python e SQLite diretamente.
- Arquivo principal:  `app.py` 

### 2️⃣ Executar Localmente
#### Pré-requisitos:
- Um navegador atualizado (Google Chrome, Firefox, Edge, etc.).


#### Etapas:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-projeto

2. Crie um ambiente virtual (passo obrigatório):
 python -m venv venv
 source venv/Scripts/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Inicie o servidor:
pyhton app.py

A API estará disponível em https://api-livros-1jof.onrender.com


Esta é uma API simples feita com Flask e SQLite para fins de estudo na escola Vai Na Web, que permite cadastrar e listar os livros doados, adaptados a telas diferentes através do SASS.


## Stack utilizada

Python
SQLite
Flask
CORS




## Endpoints

```POST/doar
O endpoint /doar é utilizado para cadastrar um novo livro em nossa API.

Envio de informações (JSON):

{
    "Título":"Senhor das Moscas",
    "categoria": "Romance",
    "autor": "William Golding",
    "image_url": "https://m.media-amazon.com/images/I/51m-yU8YQCS._SY445_SX342_.jpg"
}

Resposta (201):
{
    "mensagem": "Livro cadastrado com sucesso!"
}

GET /livros

O endpoint /livros retorna todos os livros cadastrados na API

Resposta (200):

{
    "id": "1",
    "titulo": "A Viagem do Peregrino da Alvorada",
    "categoria": "Crônica",
    "autor": "C.S. Lewis",
    "image_url": "https://m.media-amazon.com/images/I/71rHFeIWJKL._SY385_.jpg"
}
```


## Aprendizados

Criar uma API em Flask

## Funcionalidades

- Fazer a doação de um livro e ver na parte "livros doados"

- Preview em tempo real

- Modo tela cheia

- Multiplataforma


## 🔗 Links
https://github.com/TulaniSouza/api_t2.git

https://api-livros-1jof.onrender.com

https://github.com/TulaniSouza/

https://www.linkedin.com/tulani-souza


