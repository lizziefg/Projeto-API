# **Gerenciador de Processos Jurídicos**

Terceiro Mini Projeto da Disciplina Linguagem de Programação II (Fatec Rio Claro).

## **📝 Descrição do Projeto**

Este projeto implementa um servidor de API (backend) e um cliente (consumidor) para simular um sistema de gerenciamento de processos jurídicos. O objetivo é demonstrar a criação e o consumo de APIs em Python, conforme a proposta do Terceiro Mini Projeto.

O sistema permite:

* Cadastrar novos processos.  
* Listar todos os processos cadastrados.  
* Buscar um processo específico pelo seu número.  
* Deletar um processo.

## **🚀 Tecnologias Utilizadas**

* **Python 3.10+**  
* **FastAPI:** Para a criação do servidor da API (backend).  
* **Uvicorn:** Para rodar o servidor FastAPI.  
* **Requests:** Para o consumo da API pelo cliente.  
* **Pydantic:** Para validação de dados no servidor (integrado ao FastAPI).

## **⚙️ Instalação e Configuração**

Siga os passos abaixo para configurar o ambiente e executar o projeto.

### **1\. Crie um Ambiente Virtual**

É altamente recomendado criar um ambiente virtual para isolar as dependências do projeto.

python \-m venv .venv

### **2\. Ative o Ambiente Virtual**

* **No Windows (PowerShell):**

.\\.venv\\Scripts\\Activate

* **No macOS/Linux:**

source .venv/bin/activate

### **3\. Instale as Dependências**

Com o ambiente ativado, instale todos os pacotes necessários:

pip install \-r requirements.txt

## **🏃‍♂️ Como Executar**

Para rodar o projeto, você precisará de **dois terminais** abertos na raiz do projeto (com o ambiente virtual ativado em ambos).

### **1\. Terminal 1: Rodar o Servidor (Backend)**

Navegue até a pasta da aplicação do servidor e inicie o uvicorn.

\# Navegue até a pasta do servidor

cd server/app

\# Inicie o servidor

uvicorn main:app \--reload

O servidor estará rodando em http://127.0.0.1:8000.

Você pode acessar a documentação interativa da API (gerada automaticamente pelo FastAPI) no seu navegador:

http://127.0.0.1:8000/docs

### **2\. Terminal 2: Rodar o Cliente (Frontend)**

No segundo terminal (enquanto o servidor está rodando), navegue até a pasta do cliente e execute o script main.py.

\# Navegue até a pasta do cliente

cd client

\# Execute o cliente

python main.py

Um menu interativo aparecerá, permitindo que você execute as ações de criar, listar, buscar e deletar processos.

## **🗺️ Endpoints da API**

A API expõe os seguintes endpoints (base: http://127.0.0.1:8000):

| Método | Rota | Descrição |
| :---- | :---- | :---- |
| POST | /processos/ | Cria um novo processo. |
| GET | /processos/ | Lista todos os processos cadastrados. |
| GET | /processos/{numero\_processo} | Busca um processo específico. |
| DELETE | /processos/{numero\_processo} | Deleta um processo específico. |

## **👥 Autores**

* Elisa Alcântara  
* Raphael Neves

