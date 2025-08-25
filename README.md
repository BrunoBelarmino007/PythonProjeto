# 🐍 Sistema de Cadastro de Clientes - Python com SQLite

Este projeto corresponde ao **quinto e último curso da Trilha de Conhecimento em Python** oferecida pela **Fundação Bradesco**. O sistema foi desenvolvido durante o curso **"Desenvolvendo um Projeto Completo em Python com Estruturas de Dados"** como atividade prática final.

### 🎯 Posição na Trilha de Conhecimento
- **1º Curso**: Introdução à Programação Orientada a Objetos - POO 
- **2º Curso**: Linguagem de Programação Python - Básico → [Repositório Python](https://github.com/BrunoBelarmino007/Python.git)
- **3º Curso**: Desenvolvimento Orientado a Objeto Utilizando a Linguagem Python → [Repositório PythoncomPOO](https://github.com/BrunoBelarmino007/PythoncomPOO.git)
- **4º Curso**: Criando um Projeto com Interface Gráfica Utilizando a Linguagem Python  → [Repositório PythoncomInterfaceGráfica](https://github.com/BrunoBelarmino007/PythoncomInterfaceGrafica.git)
- **5º Curso**:  **Desenvolvendo um Projeto Completo Python com Estruturas de Dados (Este repositório)** ⭐

## 🚀 Sobre o Projeto

Sistema completo de **CRUD (Create, Read, Update, Delete)** para cadastro de clientes com interface gráfica, demonstrando a aplicação prática de:

- **Interface Gráfica** com Tkinter
- **Banco de Dados SQLite** para persistência
- **Arquitetura MVC** (Model-View-Controller)
- **Programação Orientada a Objetos**
- **Validação de Dados** e tratamento de erros
- **Estruturas de Dados** avançadas

## 🏗️ Arquitetura do Sistema

### Estrutura de Arquivos
```
PythonProjeto/
├── __pycache__/          # Cache do Python (auto-gerado)
├── .gitignore            # Arquivos ignorados pelo Git
├── Aplication.py         # Controlador principal 
├── Backend.py            # Modelo de dados 
├── GUI.py                # Interface gráfica 
├── clientes.db           # Banco de dados SQLite
└── README.md             # Este arquivo
```

### Padrão de Arquitetura MVC

| Componente | Arquivo | Responsabilidade |
|------------|---------|------------------|
| **Model** | `Backend.py` | Gerenciamento de dados e operações no banco |
| **View** | `GUI.py` | Interface gráfica do usuário |
| **Controller** | `Aplication.py` | Lógica de controle e eventos |

## 🚀 Funcionalidades

### ✨ Operações CRUD Completas
- **📝 Inserir** novos clientes
- **👀 Visualizar** todos os clientes cadastrados  
- **🔍 Buscar** clientes por qualquer campo
- **✏️ Atualizar** dados de clientes existentes
- **🗑️ Deletar** clientes selecionados

### 🛡️ Validações e Segurança
- **CPF único** - Impede cadastros duplicados
- **Validação de campos** obrigatórios
- **Mensagens de feedback** para o usuário
- **Tratamento de erros** robusto

### 💾 Persistência de Dados
- **Banco SQLite** integrado
- **Auto-criação** da estrutura do banco
- **Transações seguras** com commit/rollback

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **Tkinter** - Interface gráfica nativa
- **SQLite3** - Banco de dados embutido
- **PyInstaller** - Geração de executável

## ⚙️ Como Executar

### Método 1: Executar via Python
```bash
# Clone o repositório
git clone https://github.com/BrunoBelarmino007/PythonProjeto.git
cd PythonProjeto

# Execute o sistema
python Aplication.py
```

### Método 2: Gerar Executável
```bash
# Instalar o PyInstaller
pip install pyinstaller

# Gerar o executável
pyinstaller --onefile --windowed --noconsole Aplication.py
```

O executável será gerado na pasta `dist/` e pode ser executado sem necessidade do Python instalado.

## 🗄️Estrutura do Banco de Dados

### Tabela: `clientes`

| Campo       | Tipo                | Descrição                             |
| ----------- | ------------------- | ------------------------------------- |
| `id`        | INTEGER PRIMARY KEY | Identificador único (auto-incremento) |
| `nome`      | TEXT                | Nome do cliente                       |
| `sobrenome` | TEXT                | Sobrenome do cliente                  |
| `email`     | TEXT                | Email do cliente                      |
| `cpf`       | TEXT UNIQUE         | CPF do cliente (único no sistema)     |

## 🖱️ Como Usar o Sistema

### Cadastrar Novo Cliente

1. Preencha os campos: Nome, Sobrenome, Email e CPF
2. Clique em **"Inserir"**
3. Sistema validará CPF único e confirmará o cadastro

### Buscar Clientes

1. Preencha qualquer campo com critério de busca
2. Clique em **"Buscar"**
3. Resultados aparecerão na lista

### Atualizar Cliente

1. Clique em um cliente na lista para selecioná-lo
2. Modifique os campos desejados
3. Clique em **"Atualizar Selecionados"**

### Excluir Cliente

1. Selecione um cliente na lista
2. Clique em **"Deletar Selecionados"**

## 🧩Componentes Técnicos

### TransactionObject (`Backend.py`)

Classe responsável pelo gerenciamento das operações de banco:

* Conexão/desconexão com SQLite
* Execução de queries SQL
* Persistência de transações
* Operações CRUD encapsuladas

### GUI (`GUI.py`)

Interface gráfica construída com Tkinter:

* Layout responsivo com Grid
* Componentes: Entry, Label, Listbox, Button
* Scrollbar integrada
* Estilização consistente

### Controller (`Aplication.py`)

Gerenciamento de eventos e lógica de negócio:

* Bind de eventos dos botões
* Validações de entrada
* Feedback para usuário
* Coordenação entre View e Model

## 📚 Conceitos Aplicados

### Estruturas de Dados

* **Listas** para manipulação de registros
* **Tuplas** para dados de retorno do banco
* **Dicionários** implícitos nas operações SQLite

### Programação Orientada a Objetos

* **Classes** bem definidas com responsabilidades específicas
* **Encapsulamento** de funcionalidades
* **Métodos** organizados por contexto

### Padrões de Projeto

* **MVC** para separação de responsabilidades
* **Singleton** implícito na classe TransactionObject
* **Command Pattern** nos eventos dos botões

## Conquistas de Aprendizado

Ao completar este projeto, foram consolidados:

* ✅ **Interface Gráfica**: Criação de aplicações desktop
* ✅ **Banco de Dados**: Operações SQL e persistência
* ✅ **Arquitetura**: Organização profissional de código
* ✅ **Validação**: Tratamento robusto de dados
* ✅ **Deploy**: Geração de executáveis distribuíveis
* ✅ **Debugging**: Identificação e correção de erros
* ✅ **UX**: Experiência do usuário intuitiva

---

## 🤝 Contribuições

Este repositório é para fins educacionais e faz parte de uma trilha de aprendizado. Sugestões de melhorias são bem-vindas!

---

Que possamos viver de forma justa e íntegra, amando mesmo quem nos fere, retribuindo o mal com o bem e cultivando a paz, com humildade, generosidade e plena confiança na justiça de Deus - Romanos 12:14 e 21.

---
