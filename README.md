# CRUD de Alvos com Django e PostgreSQL

Este projeto implementa um **CRUD (Create, Read, Update, Delete)** para **alvos geográficos** utilizando **Django**, **PostgreSQL** e **Docker**. Ele oferece uma interface para cadastrar, visualizar e editar alvos em um mapa interativo. Além disso, disponibiliza uma **API RESTful** para interagir com os alvos de forma programática.

## Funcionalidades
- **Cadastro de Alvos**: Adicione alvos com informações de nome, latitude, longitude e data de expiração.
- **Exibição de Alvos no Mapa**: Visualize os alvos cadastrados diretamente em um mapa interativo.
- **Formulário Modal para Inserção e Edição**: Modal com formulário para inserir e editar alvos de forma prática.
- **API RESTful**: Exposição de endpoints para criação, leitura, atualização e exclusão dos alvos.
- **Docker**: O projeto está configurado para rodar com Docker e Docker Compose, facilitando o setup e deploy.

## Tecnologias Utilizadas
- **Django**: Framework web para desenvolvimento rápido e eficiente.
- **Django REST Framework**: Para criar a API RESTful.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os alvos.
- **Docker**: Para orquestrar os containers de aplicação e banco de dados.
- **JavaScript (Fetch API)**: Para comunicação assíncrona com a API sem recarregar a página.

## Como Rodar o Projeto

### Pré-requisitos
- Docker e Docker Compose instalados na sua máquina.
