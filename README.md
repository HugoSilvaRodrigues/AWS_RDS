# Projeto de Consumo de BD em MySQL com Streamlit em Container

## Passos

### Passo 1: Criar o BD na AWS
- Crie o banco de dados na AWS.
- Deixe-o acessível publicamente.

### Passo 2: Modificar o Código
- Atualize o código com o host e a senha do novo banco de dados.
- **Observação**: Caso crie um banco de dados com um nome diferente de "mercado", altere também no código.

### Passo 3: Criar a Imagem Docker
- Utilize o Dockerfile para criar a imagem:
  ```bash
  docker build -t appweb .

### Passo 4: Iniciar o container
  ```bash
  docker run -dit -p 8501:8501 --name appweb_container appweb
