# Pagina de Cadatstro usando docker

Este projeto é uma refatoração de outro projeto antigo. Trata-se aplicação web simples construída com Python e Docker, que permite cadastrar e exibir usuários.

## Pré-requisitos

-   Docker

## Como Executar

1.  Clone este repositório:

    ```bash
    git clone https://github.com/LucasMirandaVS/textpage_docker.git
    cd textpage_docker
    ```

2.  Execute o Docker Compose:

    ```bash
    docker-compose up --build
    ```

3.  Acesse a aplicação em `http://localhost:8000`.

## Dependências

-   FastAPI
-   Uvicorn
-   Jinja2
-   python-multipart
