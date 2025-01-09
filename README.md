

# Sistema de Comparação de Preços de Imóveis

Este sistema foi desenvolvido utilizando Python e a biblioteca **CustomTkinter** para criar uma interface gráfica de fácil utilização. O sistema permite cadastrar, visualizar, editar, excluir e salvar imóveis, além de exibir uma recomendação com base no melhor preço por metro quadrado e gráficos de comparação e visualização usando a biblioteca Matplotlib.

## Funcionalidades

### 1. **Adicionar Imóvel**
   - Permite adicionar um novo apartamento ao sistema, com informações como localização, número de quartos, área e preço.
   - Valida os campos para garantir que a área e o preço sejam maiores que zero.

### 2. **Editar Imóvel**
   - Permite editar as informações de um apartamento já cadastrado.

### 3. **Excluir Imóvel**
   - Permite excluir um apartamento da lista.

### 4. **Exibir Recomendação**
   - Exibe o apartamento com o melhor preço por metro quadrado, com todas as suas informações.

### 5. **Carregar Imóveis**
   - Carrega os apartamentos a partir de um arquivo JSON previamente salvo.

### 6. **Salvar Imóveis**
   - Salva a lista de apartamentos em um arquivo JSON.

### 7. **Exibir Gráficos**
   - Exibe dois gráficos comparativos:
     - Preço dos apartamentos por localização.
     - Preço por metro quadrado dos apartamentos.

## Estrutura do Código

- **Funções principais:**
  - `calcular_preco_por_metro(preco, area)`: Calcula o preço por metro quadrado de um apartamento.
  - `adicionar_apartamento()`: Adiciona um novo apartamento ou edita um existente.
  - `carregar_apartamentos()`: Carrega apartamentos do arquivo JSON.
  - `salvar_apartamentos()`: Salva a lista de apartamentos no arquivo JSON.
  - `excluir_apartamento()`: Exclui um apartamento da lista.
  - `exibir_recomendacao()`: Exibe o apartamento com o melhor preço por metro quadrado.
  - `exibir_grafico()`: Exibe gráficos comparativos de preços dos apartamentos.

- **Interface gráfica:**
  - A interface gráfica é composta por frames e botões criados com **CustomTkinter**.
  - A interface está dividida em 3 áreas principais:
    - **Botões de Controle**: Contém os botões para adicionar, salvar, carregar, excluir, e exibir gráficos.
    - **Lista de Apartamentos**: Exibe a lista de apartamentos cadastrados.
    - **Entrada de Dados**: Permite inserir informações para adicionar ou editar apartamentos.

## Como Usar

1. **Adicionar Apartamento:**
   - Preencha os campos de "Localização", "Número de Quartos", "Área" e "Preço Total".
   - Clique em "Adicionar Imóveis" para salvar o novo apartamento.

2. **Exibir Recomendação:**
   - Clique em "Exibir Recomendação" para ver o apartamento com o melhor preço por metro quadrado.

3. **Carregar e Salvar Imóveis:**
   - Clique em "Carregar Imóveis" para carregar os apartamentos de um arquivo JSON.
   - Clique em "Salvar Imóveis" para salvar a lista de apartamentos no arquivo JSON.

4. **Exibir Gráficos:**
   - Clique em "Exibir Gráfico" para visualizar os gráficos de comparação de preços.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `customtkinter`
  - `json`
  - `matplotlib`

### Instalação das Dependências

Para instalar as dependências necessárias, execute o seguinte comando:

```bash
pip install customtkinter matplotlib
```

## Como Rodar o Sistema

1. Baixe ou clone o repositório.
2. Execute o script principal do sistema:

```bash
python mains.py
```

## Contribuições

Contribuições são bem-vindas! Se você deseja adicionar novas funcionalidades ou corrigir erros, siga os seguintes passos:

1. Faça um fork do repositório.
2. Crie uma nova branch para a sua feature.
3. Envie um pull request com a descrição das alterações feitas.
